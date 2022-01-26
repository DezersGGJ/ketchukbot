import discord
import random
import datetime
import humanize
from discord.ext import commands
from pymongo import MongoClient


class Economic(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.cluster = MongoClient("mongodb+srv://DezersGG:Weerweer333@cluster0.b9xjp.mongodb.net/ecodb?retryWrites=true&w=majority")
        self.collection = self.cluster.ecodb.colldb
        self.collserver = self.cluster.ecodb.collserver

    @commands.command()
    async def daily(self, ctx):
        if self.collection.find_one({'_id': ctx.author.id})['cddaily'] == 0:
            amount = random.randint(2000,5000)
            time = int(datetime.datetime.utcnow().timestamp())
            self.collection.update_one({"_id": ctx.author.id}, {"$set": {"cddaily": time}})
            self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": amount}})
            embed = discord.Embed(
                description = f"Твоя ежедневная награда составила <:cash:903999146569138216>{humanize.intcomma(amount)}.",
                color = 0x00ff00
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        else:
            time = self.collection.find_one({"_id": ctx.author.id})["cddaily"]
            cdtime = int(datetime.datetime.utcnow().timestamp()) - 86400
            if time < cdtime:
                amount = random.randint(2000,5000)
                time = int(datetime.datetime.utcnow().timestamp())
                self.collection.update_one({"_id": ctx.author.id}, {"$set": {"cddaily": time}})
                self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": amount}})
                embed = discord.Embed(
                    description = f"Твоя ежедневная награда составила <:cash:903999146569138216>{humanize.intcomma(amount)}.",
                    color = 0x00ff00
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
            else:
                cdtime = int(datetime.datetime.utcnow().timestamp()) - 86400
                time = self.collection.find_one({"_id": ctx.author.id})["cddaily"] - cdtime
                cooldown = str(datetime.timedelta(seconds=time))
                embed = discord.Embed(
                    description = f"<:timecooldown:911306427723841566>Вы сможете получить ежедневную награду через {cooldown}",
                    color = 0xFF2400
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)

    @commands.command()
    async def weekly(self, ctx):
        if self.collection.find_one({'_id': ctx.author.id})['cdweekly'] == 0:
            amount = random.randint(5000,20000)
            time = int(datetime.datetime.utcnow().timestamp())
            self.collection.update_one({"_id": ctx.author.id}, {"$set": {"cdweekly": time}})
            self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": amount}})
            embed = discord.Embed(
                description = f"Твоя еженедельная награда составила <:cash:903999146569138216>{humanize.intcomma(amount)}.",
                color = 0x00ff00
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        else:
            time = self.collection.find_one({"_id": ctx.author.id})["cdweekly"]
            cdtime = int(datetime.datetime.utcnow().timestamp()) - 604800
            if time < cdtime:
                amount = random.randint(5000,20000)
                time = int(datetime.datetime.utcnow().timestamp())
                self.collection.update_one({"_id": ctx.author.id}, {"$set": {"cdweekly": time}})
                self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": amount}})
                embed = discord.Embed(
                    description = f"Твоя еженедельная награда составила <:cash:903999146569138216>{humanize.intcomma(amount)}.",
                    color = 0x00ff00
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
            else:
                cdtime = int(datetime.datetime.utcnow().timestamp()) - 604800
                time = self.collection.find_one({"_id": ctx.author.id})["cdweekly"] - cdtime
                cooldown = str(datetime.timedelta(seconds=time))
                embed = discord.Embed(
                    description = f"<:timecooldown:911306427723841566>Вы сможете получить еженедельную награду через {cooldown}",
                    color = 0xFF2400
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)


def setup(bot):
    bot.add_cog(Economic(bot))
