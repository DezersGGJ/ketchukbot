import discord
import random
import datetime
import humanize
from discord.ext import commands, tasks
from pymongo import MongoClient


class Basic(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.cluster = MongoClient("mongodb+srv://DezersGG:Weerweer333@cluster0.b9xjp.mongodb.net/ecodb?retryWrites=true&w=majority")
        self.collection = self.cluster.ecodb.colldb
        self.collserver = self.cluster.ecodb.collserver

    @commands.command()
    async def avatar(ctx, member: discord.Member=None):
        if member is None:
            embed = discord.Embed(
                title = f"Аватар {ctx.author.name}",
                color = 0x00ff00
            )
            embed.set_image(url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(
                title = f"Аватар {member.name}",
                color = 0x00ff00
            )
            embed.set_image(url = member.avatar_url)
            await ctx.send(embed = embed)

    @commands.command()
    async def servericon(ctx):
        embed = discord.Embed(
            title = f"{ctx.guild.name}",
            color = 0x00ff00
        )
        embed.set_image(url = ctx.guild.icon_url)
        await ctx.send(embed = embed)

    @commands.command(aliases = ["mes"])
    async def messages(ctx, member: discord.Member = None):
        if member is None:
            umes = self.collection.find_one({"_id": ctx.author.id})["mes"]
            if umes < 149:
                embed = discord.Embed(
                    description = f"{ctx.author} имеет `{self.collection.find_one({'_id': ctx.author.id})['mes']}` сообщений. `{150 - umes}` нужно для получения <@&903385564781350962>",
                    color = 0x00ff00
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
            elif umes < 299:
                embed = discord.Embed(
                    description = f"{ctx.author} имеет `{self.collection.find_one({'_id': ctx.author.id})['mes']}` сообщений. `{300 - umes}` нужно для получения <@&905008758277681153>",
                    color = 0x00ff00
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
            elif umes < 499:
                embed = discord.Embed(
                    description = f"{ctx.author} имеет `{self.collection.find_one({'_id': ctx.author.id})['mes']}` сообщений. `{500 - umes}` нужно для получения <@&904708571156066314>",
                    color = 0x00ff00
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
            elif umes < 999:
                embed = discord.Embed(
                    description = f"{ctx.author} имеет `{self.collection.find_one({'_id': ctx.author.id})['mes']}` сообщений. `{1000 - umes}` нужно для получения <@&904712301255467058>",
                    color = 0x00ff00
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
            elif umes < 1749:
                embed = discord.Embed(
                    description = f"{ctx.author} имеет `{self.collection.find_one({'_id': ctx.author.id})['mes']}` сообщений. `{1750 - umes}` нужно для получения <@&904714252089188382>",
                    color = 0x00ff00
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
            elif umes < 2999:
                embed = discord.Embed(
                    description = f"{ctx.author} имеет `{self.collection.find_one({'_id': ctx.author.id})['mes']}` сообщений. `{3000 - umes}` нужно для получения <@&904714499804790786>",
                    color = 0x00ff00
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
            elif umes < 4999:
                embed = discord.Embed(
                    description = f"{ctx.author} имеет `{self.collection.find_one({'_id': ctx.author.id})['mes']}` сообщений. `{5000 - umes}` нужно для получения <@&904715362715721769>",
                    color = 0x00ff00
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
            elif umes > 4999:
                embed = discord.Embed(
                    description = f"{ctx.author} имеет `{self.collection.find_one({'_id': ctx.author.id})['mes']}` сообщений.",
                    color = 0x00ff00
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
        else:
            mmes = self.collection.find_one({"_id": member.id})["mes"]
            if mmes < 149:
                embed = discord.Embed(
                    description = f"{member} имеет `{self.collection.find_one({'_id': member.id})['mes']}` сообщений. `{150 - mmes}` нужно для получения <@&903385564781350962>",
                    color = 0x00ff00
                )
                embed.set_author(name=member, icon_url=member.avatar_url)
                await ctx.send(embed = embed)
            elif mmes < 299:
                embed = discord.Embed(
                    description = f"{member} имеет `{self.collection.find_one({'_id': member.id})['mes']}` сообщений. `{300 - mmes}` нужно для получения <@&905008758277681153>",
                    color = 0x00ff00
                )
                embed.set_author(name=member, icon_url=member.avatar_url)
                await ctx.send(embed = embed)
            elif mmes < 499:
                embed = discord.Embed(
                    description = f"{member} имеет `{self.collection.find_one({'_id': member.id})['mes']}` сообщений. `{500 - mmes}` нужно для получения <@&904708571156066314>",
                    color = 0x00ff00
                )
                embed.set_author(name=member, icon_url=member.avatar_url)
                await ctx.send(embed = embed)
            elif mmes < 999:
                embed = discord.Embed(
                    description = f"{member} имеет `{self.collection.find_one({'_id': member.id})['mes']}` сообщений. `{1000 - mmes}` нужно для получения <@&904712301255467058>",
                    color = 0x00ff00
                )
                embed.set_author(name=member, icon_url=member.avatar_url)
                await ctx.send(embed = embed)
            elif mmes < 1749:
                embed = discord.Embed(
                    description = f"{member} имеет `{self.collection.find_one({'_id': member.id})['mes']}` сообщений. `{1750 - mmes}` нужно для получения <@&904714252089188382>",
                    color = 0x00ff00
                )
                embed.set_author(name=member, icon_url=member.avatar_url)
                await ctx.send(embed = embed)
            elif mmes < 2999:
                embed = discord.Embed(
                    description = f"{member} имеет `{self.collection.find_one({'_id': member.id})['mes']}` сообщений. `{3000 - mmes}` нужно для получения <@&904714499804790786>",
                    color = 0x00ff00
                )
                embed.set_author(name=member, icon_url=member.avatar_url)
                await ctx.send(embed = embed)
            elif mmes < 4999:
                embed = discord.Embed(
                    description = f"{member} имеет `{self.collection.find_one({'_id': member.id})['mes']}` сообщений. `{5000 - mmes}` нужно для получения <@&904715362715721769>",
                    color = 0x00ff00
                )
                embed.set_author(name=member, icon_url=member.avatar_url)
                await ctx.send(embed = embed)
            elif mmes > 4999:
                embed = discord.Embed(
                    description = f"{member} имеет `{self.collection.find_one({'_id': member.id})['mes']}` сообщений.",
                    color = 0x00ff00
                )
                embed.set_author(name=member, icon_url=member.avatar_url)
                await ctx.send(embed = embed)

    @commands.command(aliases = ["add-messages"])
    @commands.has_any_role(902849136041295883, 506864696562024448, 902841113734447214, 933769903910060153)
    async def add_messages(ctx, amount: int, member: discord.Member = None):
        if amount > 0:
            if member is None:
                self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"mes": amount}})
                embed = discord.Embed(
                    description = f"<:check:930367892455850014>Добавлено **{amount}** сообщений {ctx.author.mention}.",
                    color = 0x00ff00
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
            else:
                self.collection.update_one({"_id": member.id}, {"$inc": {"mes": amount}})
                embed = discord.Embed(
                    description = f"<:check:930367892455850014>Добавлено **{amount}** сообщений {member.mention}",
                    color = 0x00ff00
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)


    @commands.command(aliases = ["remove-messages"])
    @commands.has_any_role(902849136041295883, 506864696562024448, 902841113734447214, 933769903910060153)
    async def remove_messages(ctx, amount: int, member: discord.Member = None):
        if amount > 0:
            if member is None:
                self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"mes": -amount}})
                embed = discord.Embed(
                    description = f"<:check:930367892455850014>Забрано **{amount}** сообщений у {ctx.author.mention}.",
                    color = 0x00ff00
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
            else:
                self.collection.update_one({"_id": member.id}, {"$set": {"mes": -amount}})
                embed = discord.Embed(
                    description = f"<:check:930367892455850014>Забрано **{amount}** сообщений у {member.mention}.",
                    color = 0x00ff00
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)

    @commands.command()
    async def ping(ctx):
        embed = discord.Embed(
            description = f"Ping: {round(self.bot.latency * 1000)}ms",
            color = 0x00ff00
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed = embed)

    @remove_messages.error
    async def remove(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Аргумент не указан.\n\nИспользование:\n`remove-messages <amount> <user>`",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.errors.BadArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Неправильно указан аргумент `<amount>`.\n\nИспользование:\n`remove-messages <amount> <user>`",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.errors.MemberNotFound):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Пользователь не найден.",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @add_messages.error
    async def add(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Аргумент не указан.\n\nИспользование:\n`add-messages <amount> <user>`",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.errors.BadArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Неправильно указан аргумент `<amount>`.\n\nИспользование:\n`add-messages <amount> <user>`",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.errors.MemberNotFound):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Пользователь не найден.",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Basic(bot))
