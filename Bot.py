import discord
import random
import youtube_dl 
import os
import asyncio
import requests
import json
import logging
import io
import asyncpg
import datetime
import urllib.request
import urllib.parse, urllib.request, re
from pathlib import Path
from bs4 import BeautifulSoup
from discord import utils
from discord.utils import get
from discord.ext import commands 
from discord.ext.commands import Bot
from PIL import Image, ImageFont, ImageDraw     #python -m pip install --upgrade Pillow 
import config

cwd=str(Path(__file__).parents[0])
print(f"{cwd}\n-------")


token = open("token.txt", 'r').read()
PREFIX = '!'
client = commands.Bot(command_prefix = PREFIX )#command prefix

client.remove_command( 'help' )
#players = {}

@client.event
async def on_ready():
    print("Bot is online!")

queues = {}

def is_connected(ctx):                                          #The function of checking for the presence of a bot in voice chat
    voice = get(client.voice_clients, guild=ctx.guild)
    return voice and voice.is_connected()



@client.command( pass_context = True, aliases=['j', 'joi'] )  #Connecting a bot to a voice chat 
async def join( ctx ):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await ctx.send(f"Joined {channel}")

@client.command( pass_context = True, aliases=['l', 'leav'] )   #Chat bot exit
async def leave( ctx ):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"The bot has left {channel}")
        await ctx.send(f"Left {channel}")
    else:
        print("Bot was told to leave voice channel, but was not in one")
        await ctx.send("Don't think I am in a voice channel")

@client.command( pass_context = True )          #Проигрывание песни с ютуба
async def play(ctx, url : str):                 
    song_there = os.path.isfile('song.mp3')     
    
    try:
        if song_there:
            os.remove('song.mp3')
            print('[log] Old file deleted')    
    except PermissionError:
        print('[log] Can`t find file')
        
    await ctx.send('Download music...')             

    voice = get(client.voice_clients, guild = ctx.guild)    

    ydl_opts = {                              
        'format' : 'bestaudio/best',
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192'
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
        print('[log] Downloading music...')
        ydl.download([url])
    
    for file in os.listdir('./'):              
        if file.endswith('.mp3'):
            name = file
            print(f'[log] Rename file: {file}')
            os.rename(file, 'song.mp3')

    voice.play(discord.FFmpegPCMAudio('song.mp3'), after = lambda e: print(f'[log] {name}, Music was ended'))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    song_name = name.rsplit('-', 2)
    await ctx.send(f'Now playing: {song_name[0]}')

@client.command()
async def youtube(ctx, *, search):

    query_string = urllib.parse.urlencode({
        'search_query': search
    })
    htm_content = urllib.request.urlopen(
        'http://www.youtube.com/results?' + query_string
    )

    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', htm_content.read().decode())
    #await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])
    url ='http://www.youtube.com/watch?v=' + search_results[0]
    song_there = os.path.isfile('song.mp3')  # (Пока что) для прекращения проигрывания команда !leave

    try:
        if song_there:
            os.remove('song.mp3')
            print('[log] Old file deleted')  # Create file of song
    except PermissionError:
        print('[log] Can`t find file')

    await ctx.send('Please waiting')  # For users

    voice = get(client.voice_clients, guild=ctx.guild)  #

    ydl_opts = {  # options of song
        'format': 'bestaudio/best',
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:  # download song from youtube on pc
        print('[log] Downloading music...')
        ydl.download([url])

    for file in os.listdir('./'):  # take song from pc
        if file.endswith('.mp3'):
            name = file
            print(f'[log] Rename file: {file}')
            os.rename(file, 'song.mp3')

    voice.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: print(f'[log] {name}, music was ended'))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    song_name = name.rsplit('-', 2)
    await ctx.send(f'Now playing: {song_name[0]}')  # send name of song in chat
    await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])

@client.command(pass_context=True, aliases=['g', 'ga', 'gam']) #game Rock-Paper-Scissors with bot 
@commands.guild_only()
async def game_rps(ctx):
    await ctx.send(
        'Привет, как твои дела ' + ctx.message.author.mention + ' ? Хочешь сыграем в камень, ножницы, бумага?')

    wins = 0
    losses = 0
    ties = 0

    while True:
        await ctx.send('%s Победы, %s Поражения, %s Ничья \n' % (wins, losses, ties))
        while True:
            await ctx.send('Что ты выберешь? (s)камень, (p)бумага, (sc)ножницы или (q)покинуть игру.')  
            player = await client.wait_for('message') 
            print(str(player))
            if player.content == 'q':
                return
            if player.content ==  's' or player.content == 'p' or player.content == 'sc':
                break
            await ctx.send('Напишите s, p, sc или q!')

        if player.content == 's':
            await ctx.send('Камень против ...')
        if player.content == 'p':
            await ctx.send('Бумага против ...')
        if player.content == 'sc':
            await ctx.send('Ножницы против ...')

        randomnum = random.randint(1, 3)
        if randomnum == 1:
            computer = 's'
            await ctx.send('Камень!')
        elif randomnum == 2:
            computer = 'p'
            await ctx.send('Бумага!')
        elif randomnum == 3:
            computer = 'sc'
            await ctx.send('Ножницы!')

        if player.content ==  computer:
            await ctx.send('Ничья!')
            ties = ties + 1
        elif player.content == 's' and computer == 'sc':
            await ctx.send('Ты победил!')
            wins = wins + 1
        elif player.content == 's' and computer == 'p':
            await ctx.send('Ты проиграл!')
            losses = losses + 1
        elif player.content == 'p' and computer == 's':
            await ctx.send('Ты победил!')
            wins = wins + 1
        elif player.content == 'p' and computer == 'sc':
            losses = losses + 1
            await ctx.send('Ты проиграл!')
        elif player.content == 'sc' and computer == 'p':
            await ctx.send('ТЫ победил!')
            wins = wins + 1
        elif player.content == 'sc' and computer == 's':
            await ctx.send('Ты проиграл!')
            losses = losses + 1    

@client.event                                                   #notification leave from server
async def on_member_remove(member):
    print(f' {member} has left a server.')

# @client.event
# async def on_member_join ( member ):                  #Need REWORK!take id from discord
# 	channel = bot.get_channel( 701052743493746809 )
# 	role = discord.utils.get ( member.guild.roles, id = 701051500704825385 )
# 	await member.add_roles( role )
# 	await channel.send( f'User {member.mention} join the server.' )

if __name__ == '__main__':
    for file in os.listdir("./cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            client.load_extension(f"cogs.{file[:-3]}")

client.run(token)                    #run client from