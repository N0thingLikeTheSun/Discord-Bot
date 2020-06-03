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
from PIL import Image, ImageFont, ImageDraw
import platform

client = commands.Bot( command_prefix = '!' )
client.remove_command( 'help' )
PREFIX = '!'

#queues = {}

def is_connected(ctx):                                          #The function of checking for the presence of a bot in voice chat
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild.id)
    return voice and voice.is_connected() 
class Commands(commands.Cog):
    def _init_(self, client):
	    self.client = client

       

    
    

    
    #@client.command( pass_context = True )
    # async def leave( ctx ):
	#     channel = ctx.message.author.voice.channel
	#     voice = get( bot.voice_clients, guild = ctx.guild )
	#     if voice and voice.is_connected():
	# 	    await voice.disconnect()
	# 	    await ctx.send( f'Bot leave { channel } channel.' )
	#     else:
	# 	    voice = await channel.connect()
    

    # @client.command()
    # async def youtube(self,ctx, *, search):

    #     query_string = urllib.parse.urlencode({
    #         'search_query': search
    #     })
    #     htm_content = urllib.request.urlopen(
    #         'http://www.youtube.com/results?' + query_string
    #     )

    #     search_results = re.findall('href="\/watch\?v=(.{11})', htm_content.read().decode())
    #     #await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])
    #     url ='http://www.youtube.com/watch?v=' + search_results[0]
    #     song_there = os.path.isfile('song.mp3')  # to stop playing the command !leave

    #     try:
    #         if song_there:
    #             os.remove('song.mp3')
    #             print('[log] Old file deleted')  # Create file of song
    #     except PermissionError:
    #         print('[log] Can`t find file')

    #     await ctx.send('Please waiting')  # For users

    #     voice = get(self.client.voice_clients, guild=ctx.guild)  #

    #     ydl_opts = {  # options of song
    #         'format': 'bestaudio/best',
    #         'postprocessors': [{
    #             'key': 'FFmpegExtractAudio',
    #             'preferredcodec': 'mp3',
    #             'preferredquality': '192'
    #         }],
    #     }

    #     with youtube_dl.YoutubeDL(ydl_opts) as ydl:  # download song from youtube on pc
    #         print('[log] Downloading music...')
    #         ydl.download([url])

    #     for file in os.listdir('./'):  # take song from pc
    #         if file.endswith('.mp3'):
    #             name = file
    #             print(f'[log] Rename file: {file}')
    #             os.rename(file, 'song.mp3')

    #     self.client.voice.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: print(f'[log] {name}, music was ended'))
    #     voice.source = discord.PCMVolumeTransformer(voice.source)
    #     voice.source.volume = 0.07

    #     song_name = name.rsplit('-', 2)
    #     await ctx.send(f'Now playing: {song_name[0]}')  # send name of song in chat
    #     await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])
    # @client.command( pass_context = True )
    # async def leave( ctx ):
	#     channel = ctx.message.author.voice.channel
	#     voice = get( bot.voice_clients, guild = ctx.guild )
	#     if voice and voice.is_connected():
	# 	    await voice.disconnect()
	# 	    await ctx.send( f'Bot leave { channel } channel.' )
	#     else:
	# 	    voice = await channel.connect()


    # @client.command( pass_context = True )          #Playing a song from YouTube
    # async def play(self, ctx, url : str):
    #                                                 #Enter command before use !join
    #     def check_queue():
    #         Queue_infile = os.path.isdir("./Queue")
    #         if Queue_infile is True:
    #             DIR = os.path.abspath(os.path.realpath("Queue"))
    #             length = len(os.listdir(DIR))
    #             still_q = length - 1
    #             try:
    #                 first_file = os.listdir(DIR)[0]
    #             except:
    #                 print("No more queued song(s)\n")
    #                 queues.clear()
    #                 return
    #             main_location = os.path.dirname(os.path.realpath(__file__))
    #             song_path = os.path.abspath(os.path.realpath("Queue") + "\\" + first_file)
    #             if length != 0:
    #                 print("Song done, playing next queued\n")
    #                 print(f"Songs still in queue: {still_q}")
    #                 song_there = os.path.isfile("song.mp3")
    #                 if song_there:
    #                     os.remove("song.mp3")
    #                 shutil.move(song_path, main_location)
    #                 for file in os.listdir("./"):
    #                     if file.endswith(".mp3"):
    #                         os.rename(file, 'song.mp3')

    #                 voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
    #                 voice.source = discord.PCMVolumeTransformer(voice.source)
    #                 voice.source.volume = 0.07

    #             else:
    #                 queues.clear()
    #                 return

    #         else:
    #             queues.clear()
    #             print("No songs were queued before the ending of the last song\n")



    #     song_there = os.path.isfile("song.mp3")
    #     try:
    #         if song_there:
    #             os.remove("song.mp3")
    #             queues.clear()
    #             print("Removed old song file")
    #     except PermissionError:
    #         print("Trying to delete song file, but it's being played")
    #         await ctx.send("ERROR: Music playing")
    #         return


    #     Queue_infile = os.path.isdir("./Queue")
    #     try:
    #         Queue_folder = "./Queue"
    #         if Queue_infile is True:
    #             print("Removed old Queue Folder")
    #             shutil.rmtree(Queue_folder)
    #     except:
    #         print("No old Queue folder")

    #     await ctx.send("Getting everything ready now")

    #     voice = get(client.voice_clients, guild=ctx.guild)

    #     ydl_opts = {
    #         'format': 'bestaudio/best',
    #         'quiet': True,
    #         'postprocessors': [{
    #             'key': 'FFmpegExtractAudio',
    #             'preferredcodec': 'mp3',
    #             'preferredquality': '192',
    #         }],
    #     }

    #     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #         print("Downloading audio now\n")
    #         ydl.download([url])

    #     for file in os.listdir("./"):
    #         if file.endswith(".mp3"):
    #             name = file
    #             print(f"Renamed File: {file}\n")
    #             os.rename(file, "song.mp3")

    #     voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
    #     voice.source = discord.PCMVolumeTransformer(voice.source)
    #     voice.source.volume = 0.07

    #     nname = name.rsplit("-", 2)
    #     await ctx.send(f"Playing: {nname[0]}")
    #     print("playing\n")
    
    

    # @client.command(pass_context=True, aliases=['q', 'que'])
    # async def queue(self,ctx, url: str):
    #     Queue_infile = os.path.isdir("./Queue")
    #     if Queue_infile is False:
    #         os.mkdir("Queue")
    #     DIR = os.path.abspath(os.path.realpath("Queue"))
    #     q_num = len(os.listdir(DIR))
    #     q_num += 1
    #     add_queue = True
    #     while add_queue:
    #         if q_num in queues:
    #             q_num += 1
    #         else:
    #             add_queue = False
    #             queues[q_num] = q_num

    #     queue_path = os.path.abspath(os.path.realpath("Queue") + f"\song{q_num}.%(ext)s")

    #     ydl_opts = {
    #         'format': 'bestaudio/best',
    #         'quiet': True,
    #         'outtmpl': queue_path,
    #         'postprocessors': [{
    #             'key': 'FFmpegExtractAudio',
    #             'preferredcodec': 'mp3',
    #             'preferredquality': '192',
    #         }],
    #     }

    #     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #         print("Downloading audio now\n")
    #         ydl.download([url])
    #     await ctx.send("Adding song " + str(q_num) + " to the queue")

    #     print("Song added to queue\n")

    # @client.command( pass_context = True )  #help user
    # async def help (self, ctx ):
    #     emb = discord.Embed( title = 'Help info:' )
    #     emb.add_field( name = '{}clear'.format( '!' ), value = 'Clean chat menu.')
    #     emb.add_field( name = '{}kick'.format( '!' ), value = 'Kick user from server.')
    #     emb.add_field( name = '{}ban'.format( '!' ), value = 'Ban user.')
    #     emb.add_field( name = '{}unban'.format( '!' ), value = 'Unban user.')
    #     await ctx.send ( embed = emb )
    

    @client.command( pass_context = True )  #view time in Kiev now
    async def time (self, ctx):
        emb = discord.Embed(title ='Kiev time:', colour=discord.Color.green(), url ='http://timenow.in.ua')
        emb.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
        emb.set_footer( text = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.set_image( url = 'https://s3.tproger.ru/uploads/2015/10/clock-1.jpg' )
        now = datetime.datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        emb.add_field( name = 'Time :', value = 'Time : {}'.format( date_time ) )
        await ctx.send ( embed = emb )

    # @client.command(pass_context=True, aliases=['s', 'sto'])
    # async def stop(self,ctx):
    #     voice = get(self.client.voice_clients, guild=ctx.guild)

    #     queues.clear()

    #     if voice and voice.is_playing():
    #         print("Music stopped")
    #         voice.stop()
    #         await ctx.send("Music stopped")
    #     else:
    #         print("No music playing failed to stop")
    #         await ctx.send("No music playing failed to stop")


    # queues = {}

    

    @client.command( pass_context = True )
    @commands.has_permissions ( administrator = True )

    async def user_mute (self, ctx, member: discord.Member ):   #mute user
    	await ctx.channel.purge( limit = 1 )
    	mute_role = discord.utils.get ( ctx.message.guild.roles, name = 'Muted' )
    	await member.add_roles( mute_role )
    	await ctx.send( f'User {member.mention} was muted.' )

    @client.command( pass_context = True )                          #kick user from server
    @commands.has_permissions( administrator = True )
    async def kick(self,ctx, member : discord.Member, *, reason=None, amount = 1):
        await ctx.channel.purge( limit = amount)
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention}')

    @client.command( pass_context = True )                          #ban user on server
    @commands.has_permissions( administrator = True )
    async def ban(self, ctx, member : discord.Member, *,reason=None, amount = 1): 
        await ctx.channel.purge( limit = amount)
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

    @client.command( pass_context = True )                           #delete last 10 msg in chat
    @commands.has_permissions( administrator = True )
    async def clear(self, ctx, amount = 5): 
        await ctx.channel.purge( limit = amount)

    @client.command( pass_context = True )                             #delete last msg in chat
    @commands.has_permissions( administrator = True )
    async def delete(self, ctx, amount = 2): 
        await ctx.channel.purge( limit = amount)

    @client.command()   #roll random numbers
    async def roll(self,ctx, dice: str):
        try:
            rolls, limit = map(int, dice.split('.'))
        except Exception:
            await ctx.send('Format has to be in N.N!')
            return
        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    
    

    @client.command( pass_context = True )                          #unban user on server must
    @commands.has_permissions( administrator = True )               #must contain username and discriminator
    async def unban(self, ctx, amount = 1, *, member):                    #Example input: !unban TestUser#1234
        await ctx.channel.purge( limit = amount)
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

    @client.command(pass_context=True, aliases=['me','mycard']) 
    async def card(self, ctx):                                      #user card
        await ctx.channel.purge(limit = 1)

        img = Image.new('RGBA', (400, 200), '#232529')
        url = str(ctx.author.avatar_url)[:-10]

        response = requests.get(url, stream = True)
        response = Image.open(io.BytesIO(response.content))
        response = response.convert('RGBA')
        response = response.resize((100, 100), Image.ANTIALIAS)

        img.paste(response, (15, 15, 115, 115))

        idraw = ImageDraw.Draw(img)
        name = ctx.author.name
        tag = ctx.author.discriminator

        headline = ImageFont.truetype('arial.ttf', size = 20)
        undertext = ImageFont.truetype('arial.ttf', size = 12)

        idraw.text((145, 15), f'{name}#{tag}', font = headline)
        idraw.text((145, 50), f'ID: {ctx.author.id}', font = undertext)

        img.save('user_card.png')
        await ctx.send(file = discord.File(fp = 'user_card.png'))

def setup(client):
	client.add_cog(Commands(client))