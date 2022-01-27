import discord
import random
import datetime
import humanize
from discord.ext import commands, tasks
from pymongo import MongoClient


class Economic(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.cluster = MongoClient("mongodb+srv://DezersGG:Weerweer333@cluster0.b9xjp.mongodb.net/ecodb?retryWrites=true&w=majority")
        self.collection = self.cluster.ecodb.colldb
        self.collserver = self.cluster.ecodb.collserver

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def work(self, ctx):
        if self.collection.find_one({"_id": ctx.author.id})["cdwork"] > 0:
            amount = random.randint(300,600)
            self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": amount}})
            self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"cdwork": -10}})
            embed = discord.Embed(
                description = f"Твоя зарплата составила <:cash:903999146569138216>{humanize.intcomma(amount)}.",
                color = 0x00ff00
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(
                    description = f"<:timecooldown:911306427723841566>Вы слишком устали.",
                    color = 0xFF2400
                )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)


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
    async def roulette(self, ctx, color, amount: int):
        num = {
            0: "green",
            1: "red",
            3: "red",
            5: "red",
            7: "red",
            9: "red",
            12: "red",
            14: "red",
            16: "red",
            18: "red",
            19: "red",
            21: "red",
            23: "red",
            25: "red",
            27: "red",
            30: "red",
            32: "red",
            34: "red",
            36: "red",
            2: "black",
            4: "black",
            6: "black",
            8: "black",
            10: "black",
            11: "black",
            13: "black",
            15: "black",
            17: "black",
            20: "black",
            22: "black",
            24: "black",
            26: "black",
            28: "black",
            29: "black",
            31: "black",
            33: "black",
            35: "black",
        }
        colors = ["red", "black", "green"]
        data = self.collection.find_one({"_id": ctx.author.id})
        minbet, maxbet = 1000, 10000
        rand = random.randint(0,36)
        if color not in colors:
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Неправильно указан аргумент `<red|black|green>`.\n\nИспользование:\n`roulette <red|black|green> <amount>`",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            return await ctx.send(embed = embed)
        else:
            if amount < minbet:
                embed = discord.Embed(
                    description = f"<:noe:911292323365781515>Минимальная ставка <:cash:903999146569138216>{humanize.intcomma(minbet)}.",
                    color = 0xff2400
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                return await ctx.send(embed = embed)
            else:
                if amount > maxbet:
                    embed = discord.Embed(
                        description = f"<:noe:911292323365781515>Максимальная ставка <:cash:903999146569138216>{humanize.intcomma(maxbet)}.",
                        color = 0xff2400
                    )
                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    return await ctx.send(embed = embed)
                else:
                    if amount > data["money"]:
                        embed = discord.Embed(
                            description = f"<:noe:911292323365781515>У вас недостаточно средств.",
                            color = 0xff2400
                        )
                        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                        return await ctx.send(embed = embed)
                    else:
                        if color == num[rand]:
                            if num[rand] == "red":
                                self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": amount}})
                                embed = discord.Embed(
                                    description = f"Выпал красный и вы выйграли.",
                                    color = 0x00ff00
                                )
                                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                return await ctx.send(embed = embed)
                            elif num[rand] == "black":
                                self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": amount}})
                                embed = discord.Embed(
                                    description = f"Выпал чёрный и вы выйграли.",
                                    color = 0x00ff00
                                )
                                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                return await ctx.send(embed = embed)
                            elif num[rand] == "green":
                                self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": amount * 14}})
                                embed = discord.Embed(
                                    description = f"Выпал зелёный и вы выйграли.",
                                    color = 0x00ff00
                                )
                                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                return await ctx.send(embed = embed)
                        else:
                            self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": -amount}})
                            if num[rand] == "red":
                                embed = discord.Embed(
                                    description = f"Выпал красный и вы проиграли.",
                                    color = 0xff2400
                                )
                                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                return await ctx.send(embed=embed)
                            elif num[rand] == "black":
                                embed = discord.Embed(
                                    description = f"Выпал чёрный и вы проиграли.",
                                    color = 0xff2400
                                )
                                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                return await ctx.send(embed = embed)
                            elif num[rand] == "green":
                                embed = discord.Embed(
                                    description = f"Выпал зелёный и вы проиграли.",
                                    color = 0xff2400
                                )
                                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                return await ctx.send(embed = embed)


    @commands.command(aliases = ["balance"])
    async def bal(self, ctx, member: discord.Member = None):
        if member is None:
            total = self.collection.find_one({'_id': ctx.author.id})['money'] + self.collection.find_one({'_id': ctx.author.id})['bank']
            embed = discord.Embed(
                description = f"Баланс:\n<:cash:903999146569138216>{humanize.intcomma(self.collection.find_one({'_id': ctx.author.id})['money'])}\nБанк:\n<:cash:903999146569138216>{humanize.intcomma(self.collection.find_one({'_id': ctx.author.id})['bank'])}\nОбщий баланс:\n<:cash:903999146569138216>{humanize.intcomma(total)}",
                color = 0x00ff00
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        else:
            total = self.collection.find_one({'_id': member.id})['money'] + self.collection.find_one({'_id': member.id})['bank']
            embed = discord.Embed(
                description = f"Баланс:\n<:cash:903999146569138216>{humanize.intcomma(self.collection.find_one({'_id': member.id})['money'])}\nБанк:\n<:cash:903999146569138216>{humanize.intcomma(self.collection.find_one({'_id': member.id})['bank'])}\nОбщий баланс:\n<:cash:903999146569138216>{humanize.intcomma(total)}",
                color = 0x00ff00
            )
            embed.set_author(name=member, icon_url=member.avatar_url)
            await ctx.send(embed = embed)

    @commands.command()
    async def pay(self, ctx, member: discord.Member, amount: int):
        data_author = self.collection.find_one({"_id": ctx.author.id})
        data_member = self.collection.find_one({"_id": member.id})
        if amount <= 0:
            embed = discord.Embed(
                description = "Введите число больше 0.",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            return await ctx.send(embed = embed)
        else:
            if data_author["money"] < amount:
                embed = discord.Embed(
                    description = f"<:noe:911292323365781515>У вас недостаточно средств.",
                    color = 0xff2400
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                return await ctx.send(embed = embed)
            else:
                self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": -amount}})
                self.collection.update_one({"_id": member.id}, {"$inc": {"money": amount}})
                embed = discord.Embed(
                    description = f"{ctx.author} перевёл {member} <:cash:903999146569138216>{humanize.intcomma(amount)}",
                    color = 0x00ff00
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                return await ctx.send(embed = embed)



def setup(bot):
    bot.add_cog(Economic(bot))
