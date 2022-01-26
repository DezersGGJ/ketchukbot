import discord
from discord.ext import commands
from pymongo import MongoClient


class Economic(commands.Cog):

	def __init__(self, bot):
		self.bot = bot
		self.cluster = MongoClient("mongodb+srv://DezersGG:Weerweer333@cluster0.b9xjp.mongodb.net/ecodb?retryWrites=true&w=majority")
		self.collection = self.cluster.ecodb.colldb
		self.collserver = self.cluster.ecodb.collserver

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.bot == False:
			if message.channel.id == 902855972509327400:
				data = collection.find_one({"_id": message.author.id})
				collection.update_one({"_id": message.author.id}, {"$inc": {"mes": 1}})
				collection.update_one({"_id": message.author.id}, {"$inc": {"money": 100}})
				if data["mes"] == 149:
					guild = bot.get_guild(message.guild.id)
					role_id = guild.get_role(903385564781350962)
					await message.author.add_roles(role_id)
				elif data["mes"] == 299:
					guild = bot.get_guild(message.guild.id)
					role_id = guild.get_role(905008758277681153)
					await message.author.add_roles(role_id)
				elif data["mes"] == 499:
					guild = bot.get_guild(message.guild.id)
					role_id = guild.get_role(904708571156066314)
					await message.author.add_roles(role_id)
				elif data["mes"] == 999:
					guild = bot.get_guild(message.guild.id)
					role_id = guild.get_role(904712301255467058)
					await message.author.add_roles(role_id)
				elif data["mes"] == 1749:
					guild = bot.get_guild(message.guild.id)
					role_id = guild.get_role(904714252089188382)
					await message.author.add_roles(role_id)
				elif data["mes"] == 2999:
					guild = bot.get_guild(message.guild.id)
					role_id = guild.get_role(904714499804790786)
					await message.author.add_roles(role_id)
				elif data["mes"] == 4999:
					guild = bot.get_guild(message.guild.id)
					role_id = guild.get_role(904715362715721769)
					await message.author.add_roles(role_id)

		await commands.process_commands(message)


def setup(bot):
	bot.add_cog(Economic(bot))