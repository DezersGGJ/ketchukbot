import discord
import random
import datetime
import humanize
from discord.ext import commands, tasks
from pymongo import MongoClient
from typing import Union

class Economic(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.cluster = MongoClient("mongodb+srv://DezersGG:Weerweer333@cluster0.b9xjp.mongodb.net/ecodb?retryWrites=true&w=majority")
        self.collection = self.cluster.ecodb.colldb
        self.collserver = self.cluster.ecodb.collserver
     
    @commands.command()
    async def daily(self, ctx):
        if self.collection.find_one({'_id': ctx.author.id})['cddaily'] == 0:
            amount = random.randint(4000,10000)
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
                amount = random.randint(4000,10000)
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
            amount = random.randint(20000,50000)
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
                amount = random.randint(20000,50000)
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
            await ctx.send(embed = embed)
        else:
            if amount < minbet:
                embed = discord.Embed(
                    description = f"<:noe:911292323365781515>Минимальная ставка <:cash:903999146569138216>{humanize.intcomma(minbet)}.",
                    color = 0xff2400
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
            else:
                if amount > maxbet:
                    embed = discord.Embed(
                        description = f"<:noe:911292323365781515>Максимальная ставка <:cash:903999146569138216>{humanize.intcomma(maxbet)}.",
                        color = 0xff2400
                    )
                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    await ctx.send(embed = embed)
                else:
                    if amount > data["money"]:
                        embed = discord.Embed(
                            description = f"<:noe:911292323365781515>У вас недостаточно средств.",
                            color = 0xff2400
                        )
                        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                        await ctx.send(embed = embed)
                    else:
                        if color == num[rand]:
                            if num[rand] == "red":
                                self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": amount}})
                                embed = discord.Embed(
                                    description = f"Выпал красный и вы выйграли.",
                                    color = 0x00ff00
                                )
                                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                await ctx.send(embed = embed)
                            elif num[rand] == "black":
                                self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": amount}})
                                embed = discord.Embed(
                                    description = f"Выпал чёрный и вы выйграли.",
                                    color = 0x00ff00
                                )
                                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                await ctx.send(embed = embed)
                            elif num[rand] == "green":
                                self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": amount * 14}})
                                embed = discord.Embed(
                                    description = f"Выпал зелёный и вы выйграли.",
                                    color = 0x00ff00
                                )
                                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                await ctx.send(embed = embed)
                        else:
                            self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": -amount}})
                            if num[rand] == "red":
                                embed = discord.Embed(
                                    description = f"Выпал красный и вы проиграли.",
                                    color = 0xff2400
                                )
                                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                await ctx.send(embed=embed)
                            elif num[rand] == "black":
                                embed = discord.Embed(
                                    description = f"Выпал чёрный и вы проиграли.",
                                    color = 0xff2400
                                )
                                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                await ctx.send(embed = embed)
                            elif num[rand] == "green":
                                embed = discord.Embed(
                                    description = f"Выпал зелёный и вы проиграли.",
                                    color = 0xff2400
                                )
                                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                await ctx.send(embed = embed)

    @roulette.error
    async def roulette_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Аргумент не указан.\n\nИспользование:\n`#roulette <red|black|green> <amount>`",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        elif isinstance(error, commands.errors.BadArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Неправильно указан аргумент `<amount>`.\n\nИспользование:\n`#roulette <red|black|green> <amount>`",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)


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

    @bal.error
    async def balance_error(self, ctx, error):
        if isinstance(error, commands.errors.MemberNotFound):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Пользователь не найден.",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)

    @commands.command()
    async def pay(self, ctx, member: discord.Member, amount: int):
        data_author = self.collection.find_one({"_id": ctx.author.id})
        data_member = self.collection.find_one({"_id": member.id})
        if amount <= 0:
            embed = discord.Embed(
                description = "Введите сумму больше <:cash:903999146569138216>0.",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        else:
            if data_author["money"] < amount:
                embed = discord.Embed(
                    description = f"<:noe:911292323365781515>У вас недостаточно средств.",
                    color = 0xff2400
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
            else:
                self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": -amount}})
                self.collection.update_one({"_id": member.id}, {"$inc": {"money": amount}})
                embed = discord.Embed(
                    description = f"{ctx.author} перевёл {member} <:cash:903999146569138216>{humanize.intcomma(amount)}",
                    color = 0x00ff00
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)

    @commands.command(aliases = ["dep"])
    async def deposit(self, ctx, amount: Union[int, str]):
        data = self.collection.find_one({"_id": ctx.author.id})
        if amount == "all":
            if data["money"] <= 0:
                embed = discord.Embed(
                    description = f"<:noe:911292323365781515>У вас на балансе <:cash:903999146569138216>0.",
                    color = 0xff2400
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
            else:
                self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"bank": data["money"]}})
                self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": -data["money"]}})
                embed = discord.Embed(
                    description = f"Вы пополнили банковский счёт на <:cash:903999146569138216>{humanize.intcomma(data['money'])}.",
                    color = 0x00ff00
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
        else:
            if data["money"] < amount:
                embed = discord.Embed(
                    description = f"<:noe:911292323365781515>У вас недостаточно средств.",
                    color = 0xff2400
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
            else:
                if amount <= 0:
                    embed = discord.Embed(
                        description = "Введите сумму больше <:cash:903999146569138216>0.",
                        color = 0xff2400
                    )
                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    await ctx.send(embed = embed)
                else:
                    self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"bank": amount}})
                    self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": -amount}})
                    embed = discord.Embed(
                        description = f"Вы пополнили банковский счёт на <:cash:903999146569138216>{humanize.intcomma(amount)}.",
                        color = 0x00ff00
                    )
                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    await ctx.send(embed = embed)

    @deposit.error
    async def deposit_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandInvokeError):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Неправильно указан аргумент `<amount>`.\n\nИспользование:\n`#deposit <amount or all>`",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        elif isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Аргумент не указан.\n\nИспользование:\n`#deposit <amount or all>`",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)

    @commands.command(aliases = ["with"])
    async def withdraw(self, ctx, amount: Union[int, str]):
        data = self.collection.find_one({"_id": ctx.author.id})
        if amount == "all":
            if data["bank"] <= 0:
                embed = discord.Embed(
                    description = f"<:noe:911292323365781515>У вас на балансе <:cash:903999146569138216>0.",
                    color = 0xff2400
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
            else:
                self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": data["bank"]}})
                self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"bank": -data["bank"]}})
                embed = discord.Embed(
                    description = f"Вы сняли с банковского счёта <:cash:903999146569138216>{humanize.intcomma(data['bank'])}.",
                    color = 0x00ff00
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
        else:
            if data["bank"] < amount:
                embed = discord.Embed(
                    description = f"<:noe:911292323365781515>У вас недостаточно средств.",
                    color = 0xff2400
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
            else:
                if amount <= 0:
                    embed = discord.Embed(
                        description = "Введите сумму больше <:cash:903999146569138216>0.",
                        color = 0xff2400
                    )
                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    await ctx.send(embed = embed)
                else:
                    self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": amount}})
                    self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"bank": -amount}})
                    embed = discord.Embed(
                        description = f"Вы cняли с банковского счёта <:cash:903999146569138216>{humanize.intcomma(amount)}.",
                        color = 0x00ff00
                    )
                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    await ctx.send(embed = embed)

    @withdraw.error
    async def withdraw_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandInvokeError):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Неправильно указан аргумент `<amount>`.\n\nИспользование:\n`#withdraw <amount or all>`",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        elif isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Аргумент не указан.\n\nИспользование:\n`#withdraw <amount or all>`",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)

    @commands.command(aliases = ["add-money"])
    @commands.has_any_role(902849136041295883, 933769903910060153, 902841113734447214)
    async def add_money(self, ctx, amount: int, member: discord.Member = None):
        if amount > 0:
            if member is None:
                self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": amount}})
                embed = discord.Embed(
                    description = f"<:check:930367892455850014>Добавлено<:cash:903999146569138216>**{humanize.intcomma(amount)}** на баланс {ctx.author.mention}.",
                    color = 0x00ff00
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
            else:
                self.collection.update_one({"_id": member.id}, {"$inc": {"money": amount}})
                embed = discord.Embed(
                    description = f"<:check:930367892455850014>Добавлено<:cash:903999146569138216>**{humanize.intcomma(amount)}** на баланс {member.mention}.",
                    color = 0x00ff00
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)

    @add_money.error
    async def addm(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Аргумент не указан.\n\nИспользование:\n`#add-money <amount> <user>`",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.errors.BadArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Неправильно указан аргумент `<amount>`.\n\nИспользование:\n`#add-money <amount> <user>`",
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
        elif isinstance(error, commands.errors.MissingAnyRole):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>У вас недостаточно прав.",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @commands.command(aliases = ["remove-money"])
    @commands.has_any_role(902849136041295883, 933769903910060153, 902841113734447214)
    async def remove_money(self, ctx, amount: int, member: discord.Member = None):
        if amount > 0:
            if member is None:
                self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": -amount}})
                embed = discord.Embed(
                    description = f"<:check:930367892455850014>Забрано<:cash:903999146569138216>**{humanize.intcomma(amount)}** с баланса {ctx.author.mention}.",
                    color = 0x00ff00
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
            else:
                self.collection.update_one({"_id": member.id}, {"$inc": {"money": -amount}})
                embed = discord.Embed(
                    description = f"<:check:930367892455850014>Забрано<:cash:903999146569138216>**{humanize.intcomma(amount)}** с баланса {member.mention}.",
                    color = 0x00ff00
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)

    @remove_money.error
    async def removem(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Аргумент не указан.\n\nИспользование:\n`#remove-money <amount> <user>`",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.errors.BadArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Неправильно указан аргумент `<amount>`.\n\nИспользование:\n`#remove-money <amount> <user>`",
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
        elif isinstance(error, commands.errors.MissingAnyRole):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>У вас недостаточно прав.",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @commands.command(aliases=["cf"])
    async def coinflip(self, ctx, amount: int, coin = "heads"):
        coins = ["heads", "tails"]
        choice = random.choice(coins)
        data = self.collection.find_one({"_id": ctx.author.id})
        minbet, maxbet = 1000, 10000
        if coin not in coins:
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Неправильно указан аргумент `<heads|tails>`.\n\nИспользование:\n`#coinflip <amount> <heads|tails>`",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        else:
            if amount < minbet:
                embed = discord.Embed(
                    description = f"<:noe:911292323365781515>Минимальная ставка <:cash:903999146569138216>{humanize.intcomma(minbet)}.",
                    color = 0xff2400
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
            else:
                if amount > maxbet:
                    embed = discord.Embed(
                        description = f"<:noe:911292323365781515>Максимальная ставка <:cash:903999146569138216>{humanize.intcomma(maxbet)}.",
                        color = 0xff2400
                    )
                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    await ctx.send(embed = embed)
                else:
                    if amount > self.collection.find_one({"_id": ctx.author.id})["money"]:
                        embed = discord.Embed(
                            description = f"<:noe:911292323365781515>У вас недостаточно средств.",
                            color = 0xff2400
                        )
                        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                        await ctx.send(embed = embed)
                    else:
                        if coin == choice:
                            if choice == "heads":
                                self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": amount}})
                                embed = discord.Embed(
                                    description = f"Выпал орёл и вы выйграли.",
                                    color = 0x00ff00
                                )
                                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                await ctx.send(embed = embed)
                            elif choice == "tails":
                                self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": amount}})
                                embed = discord.Embed(
                                    description = f"Выпала решка и вы выйграли.",
                                    color = 0x00ff00
                                )
                                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                await ctx.send(embed = embed)
                        else:
                            if choice == "heads":
                                self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": -amount}})
                                embed = discord.Embed(
                                    description = f"Выпал орёл и вы проиграли.",
                                    color = 0xff2400
                                )
                                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                await ctx.send(embed = embed)
                            elif choice == "tails":
                                self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": -amount}})
                                embed = discord.Embed(
                                    description = f"Выпала решка и вы проиграли.",
                                    color = 0xff2400
                                )
                                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                await ctx.send(embed = embed)

    @coinflip.error
    async def coinflip_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
                embed = discord.Embed(
                    description = "<:noe:911292323365781515>Аргумент не указан.\n\nИспользование:\n`#coinflip <amount> <heads|tails>`",
                    color = 0xff2400
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
        elif isinstance(error, commands.errors.BadArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Неправильно указан аргумент `<amount>`.\n\nИспользование:\n`#coinflip <amount> <heads|tails>`",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)

    @commands.command()
    async def rob(self, ctx, member: discord.Member):
        if member != ctx.author:
            if member.bot is False:
                if self.collection.find_one({"_id": ctx.author.id})["cdrob"] == 0:
                    time = int(datetime.datetime.utcnow().timestamp())
                    self.collection.update_one({"_id": ctx.author.id}, {"$set": {"cdrob": time}})
                    if random.randint(1,2) == 1:
                        if self.collection.find_one({"_id": member.id})["money"] > 100:
                            coll = self.collection.find_one({"_id": member.id})["money"]
                            ones = coll/100
                            twos = ones*20
                            self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": int(twos)}})
                            self.collection.update_one({"_id": member.id}, {"$inc": {"money": -int(twos)}})
                            embed = discord.Embed(
                                description = f"Вы ограбили {member.name} и получили <:cash:903999146569138216>{humanize.intcomma(int(twos))}.",
                                color = 0x00ff00
                            )
                            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                            await ctx.send(embed = embed)
                        else:
                            embed = discord.Embed(
                                description = f"<:noe:911292323365781515>Чтоб ограбить пользователя у него на балансе должно быть больше <:cash:903999146569138216>100.",
                                color = 0xff2400
                            )
                            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                            await ctx.send(embed = embed)
                    else:
                        amount = random.randint(1000,3000)
                        self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": -amount}})
                        embed = discord.Embed(
                            description = f"<:noe:911292323365781515>Вы были оштрафованы на <:cash:903999146569138216>{humanize.intcomma(amount)} за попытку ограбления.",
                            color = 0xff2400
                        )
                        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                        await ctx.send(embed = embed)
                else:
                    time = self.collection.find_one({"_id": ctx.author.id})["cdrob"]
                    cdtime = int(datetime.datetime.utcnow().timestamp()) - 86400
                    if time < cdtime:
                        time = int(datetime.datetime.utcnow().timestamp())
                        self.collection.update_one({"_id": ctx.author.id}, {"$set": {"cdrob": time}})
                        if random.randint(1,2) == 1:
                            if self.collection.find_one({"_id": member.id})["money"] > 100:
                                ones = self.collection.find_one({"_id": member.id})["money"] / 100
                                twos = ones * 20
                                self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": int(twos)}})
                                self.collection.update_one({"_id": member.id}, {"$inc": {"money": -int(twos)}})
                                embed = discord.Embed(
                                    description = f"Вы ограбили {member.name} и получили <:cash:903999146569138216>{humanize.intcomma(int(twos))}.",
                                    color = 0x00ff00
                                )
                                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                await ctx.send(embed = embed)
                            else:
                                embed = discord.Embed(
                                    description = f"<:noe:911292323365781515>Чтоб ограбить пользователя у него на балансе должно быть больше <:cash:903999146569138216>100.",
                                    color = 0xff2400
                                )
                                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                await ctx.send(embed = embed)
                        else:
                            amount = random.randint(1000,3000)
                            self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": -amount}})
                            embed = discord.Embed(
                                description = f"<:noe:911292323365781515>Вы были оштрафованы на <:cash:903999146569138216>{humanize.intcomma(amount)} за попытку ограбления.",
                                color = 0xff2400
                            )
                            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                            await ctx.send(embed = embed)
                    else:
                        cdtime = int(datetime.datetime.utcnow().timestamp()) - 86400
                        time = self.collection.find_one({"_id": ctx.author.id})["cdrob"] - cdtime
                        cooldown = str(datetime.timedelta(seconds=time))
                        embed = discord.Embed(
                            description = f"<:timecooldown:911306427723841566>Вы сможете ограбить пользователя через {cooldown}",
                            color = 0xFF2400
                        )
                        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                        await ctx.send(embed = embed)
            else:
                embed = discord.Embed(
                    description = f"<:noe:911292323365781515>Вы не можете ограбить себя или бота.",
                    color = 0xff2400
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
        else:
            embed = discord.Embed(
                description = f"<:noe:911292323365781515>Вы не можете ограбить себя или бота.",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)

    @rob.error
    async def rob_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Аргумент не указан.\n\nИспользование:\n`#remove-money <amount> <user>`",
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

    @commands.command()
    async def lb(self, ctx):
        lb = self.collection.find().sort("money", -1)
        i = 1
        embed = discord.Embed(
            title = "Leaderboard",
            color = 0x00ff00
        )
        for x in lb:
            try:
                temp = ctx.guild.get_member(x["_id"])
                tempmoney = x["money"]
                embed.add_field(name="", value=f"`{i}.` {temp.name} - {humanize.intcomma(int(tempmoney))}", inline=False)
                i += 1
            except:
                pass
            if i == 11:
                break
        await ctx.send(embed=embed)

            
def setup(bot):
    bot.add_cog(Economic(bot))
