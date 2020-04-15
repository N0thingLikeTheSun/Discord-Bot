import discord
import random
from discord import utils
from discord.ext import commands 
from discord.ext.commands import Bot

import config
PREFIX = '!'
client = commands.Bot(command_prefix = PREFIX )#command prefix
client.remove_command( 'help' )
# @client.command(pass_context=True)
# async def info(ctx,user: discord.User):
#     await client.say(user.joined_at)

class MyClient(discord.Client): 
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == config.POST_ID:
            channel = self.get_channel(payload.channel_id) #Get object from channel
            message = await channel.fetch_message(payload.message_id) # get object message
            member = utils.get(message.guild.members, id=payload.user_id) #get object from user who set the reaction
 
            try:
                emoji = str(payload.emoji) # emoji that set user
                role = utils.get(message.guild.roles, id=config.ROLES[emoji]) #object of the selected role (if any)
           
                if(len([i for i in member.roles if i.id not in config.EXCROLES]) <= config.MAX_ROLES_PER_USER):
                    await member.add_roles(role)
                    print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))
                else:
                    await message.remove_reaction(payload.emoji, member)
                    print('[ERROR] Too many roles for user {0.display_name}'.format(member))
           
            except KeyError as e:
                print('[ERROR] KeyError, no role found for ' + emoji)
            except Exception as e:
                print(repr(e))
 
    async def on_raw_reaction_remove(self, payload):
        channel = self.get_channel(payload.channel_id) # get object channel
        message = await channel.fetch_message(payload.message_id) # get object message
        member = utils.get(message.guild.members, id=payload.user_id) # get object from user who set the reaction
 
        try:
            emoji = str(payload.emoji) # emoji that set user
            role = utils.get(message.guild.roles, id=config.ROLES[emoji]) # object of the selected role (if any)
 
            await member.remove_roles(role)
            print('[SUCCESS] Role {1.name} has been remove for user {0.display_name}'.format(member, role))
 
        except KeyError as e:
            print('[ERROR] KeyError, no role found for ' + emoji)
        except Exception as e:
            print(repr(e))
 


@client.event
async def on_ready():
    print("Bot is online!")

@client.command( pass_context = True )
async def help( ctx, amount = 1 ):
    await ctx.channel.purge( limit = amount)
    emb = discord.Embed( title = 'DICKS ' )

    emb.add_field( name = '{}clear'.format( PREFIX ), value = 'Clear messages' )
    # emb.add_field( name = '{}clear'.format(command_prefix), value = '' )
    # emb.add_field( name = '{}clear'.format(command_prefix), value = '' )
    # emb.add_field( name = '{}clear'.format(command_prefix), value = '' )

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )
async def kick(ctx, member : discord.Member, *, reason=None, amount = 1):
    await ctx.channel.purge( limit = amount)
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )
async def ban(ctx, member : discord.Member, *,reason=None, amount = 1): 
    await ctx.channel.purge( limit = amount)
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')
    

@client.event
async def on_member_remove(member):
    print(f' {member} has left a server.')

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )
async def unban(ctx, amount = 1, *, member):
    await ctx.channel.purge( limit = amount)
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


client = MyClient()
client.run(config.TOKEN)