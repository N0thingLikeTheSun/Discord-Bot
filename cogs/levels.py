import discord
import asyncpg
import platform
from discord.ext import commands
import logging
#import cogs._json
client = commands.Bot( command_prefix = '!' )
shadow = open("shadow.txt", 'r').read()
async def create_db_pool():
	client.pg_con = await asyncpg.create_pool(database="Next_Lvl_Bot", user="postgres", password = shadow)
class  Levels(commands.Cog):
	def _init_(self, client):
		self.client = client
		#bot = commands.Bot( command_prefix = '!' )

	
	async def lvl_up(self,user):	#module for lvl-up user
		cur_xp = user['xp']
		cur_lvl = user['lvl']

		if cur_xp >= round((4*(cur_lvl ** 3))/5):
			await client.pg_con.execute(
				"""
				UPDATE users 
				   SET lvl = $1 
				 WHERE user_id = $2 
				   AND guild_id = $3
				""", cur_lvl + 1,user['user_id'], user['guild_id'])
			return True
		else:
			return False
	@commands.Cog.listener()
	@client.event
	async def on_message(self,message):
		if message.author.bot:
			return
		
		user = await client.pg_con.fetchrow(
			"""
			SELECT *
			  FROM users 
			 WHERE user_id = $1 
			   AND guild_id = $2
			""", message.author.id, message.guild.id)

		if not user:
			user = await client.pg_con.fetchrow(
				"""
				INSERT INTO users (user_id, guild_id, lvl, xp) 
					 VALUES ($1,$2,1,0)
				  RETURNING *
				""", message.author.id, message.guild.id)
		
		
		await client.pg_con.execute(
			"""UPDATE users 
				  SET xp = $1 
				WHERE user_id = $2 
				  AND guild_id = $3
			""", user['xp'] + 1, message.author.id, message.guild.id)

		if await self.lvl_up(user):
			await message.channel.send(f" {message.author.mention} is now level {user['lvl']+1 }")

	@commands.command()					#command that view lvl user
	async def stat(self, ctx, member: discord.Member = None):
		member = ctx.author if not member else member
		user = await client.pg_con.fetchrow(
			"""SELECT * FROM users 
				WHERE user_id = $1 
				  AND guild_id = $2
			""", member.id, member.guild.id)
		if not user:
			await ctx.send("Member doesn't have a level")
		else:
			
			embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
			embed.set_author(name=f"Stat user: - {member}", icon_url = ctx.author.avatar_url)
			embed.add_field(name="Number of posts", value=user['xp'])
			await ctx.send(embed=embed)

	@commands.command()					#command that view lvl user
	async def level(self, ctx, member: discord.Member = None):
		member = ctx.author if not member else member
		user = await client.pg_con.fetchrow(
			"""SELECT * FROM users 
				WHERE user_id = $1 
				  AND guild_id = $2
			""", member.id, member.guild.id)
		if not user:
			await ctx.send("Member doesn't have a level")
		else:
			embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
			embed.set_author(name=f"Level - {member}", icon_url = ctx.author.avatar_url)

			embed.add_field(name="Level", value=user['lvl'])
			embed.add_field(name="XP", value=user['xp'])
			await ctx.send(embed=embed)
client.loop.run_until_complete(create_db_pool())
def setup(client):
	client.add_cog(Levels(client))