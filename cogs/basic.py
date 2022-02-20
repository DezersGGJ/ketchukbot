import discord
import random
import datetime
import humanize
import schedule
import time
from Cybernator import Paginator
from discord.ext import commands, tasks
from pymongo import MongoClient


class Basic(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.cluster = MongoClient("mongodb+srv://DezersGG:Weerweer333@cluster0.b9xjp.mongodb.net/ecodb?retryWrites=true&w=majority")
        self.collection = self.cluster.ecodb.colldb
        self.collserver = self.cluster.ecodb.collserver

    @commands.command()
    async def avatar(self, ctx, member: discord.Member=None):
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

    @avatar.error
    async def avatar_error(self, ctx, error):
        if isinstance(error, commands.errors.MemberNotFound):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Пользователь не найден.",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @commands.command()
    async def servericon(self, ctx):
        embed = discord.Embed(
            title = f"{ctx.guild.name}",
            color = 0x00ff00
        )
        embed.set_image(url = ctx.guild.icon_url)
        await ctx.send(embed = embed)

    @commands.command(aliases = ["mes"])
    async def messages(self, ctx, member: discord.Member):
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

    @messages.error
    async def messages_error(self, ctx, error):
        if isinstance(error, commands.errors.MemberNotFound):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Пользователь не найден.",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @commands.command(aliases = ["add-messages"])
    @commands.has_any_role(902849136041295883, 506864696562024448, 902841113734447214, 933769903910060153)
    async def add_messages(self, ctx, amount: int, member: discord.Member = None):
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

    @add_messages.error
    async def add_messages_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Аргумент не указан.\n\nИспользование:\n`#add-messages <amount> <user>`",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.errors.BadArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Неправильно указан аргумент `<amount>`.\n\nИспользование:\n`#add-messages <amount> <user>`",
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

    @commands.command(aliases = ["remove-messages"])
    @commands.has_any_role(902849136041295883, 506864696562024448, 902841113734447214, 933769903910060153)
    async def remove_messages(self, ctx, amount: int, member: discord.Member = None):
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

    @remove_messages.error
    async def remove_messages_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Аргумент не указан.\n\nИспользование:\n`#remove-messages <amount> <user>`",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.errors.BadArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Неправильно указан аргумент `<amount>`.\n\nИспользование:\n`#remove-messages <amount> <user>`",
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

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(
            description = f"Ping: {round(self.bot.latency * 1000)}ms",
            color = 0x00ff00
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed = embed)

    @commands.command()
    async def help(self, ctx):
        embed1 = discord.Embed(title="⚙️Навигация по командам:", description='💎Основные:\n```\n▫️#avatar - Аватар пользователя.\n▫️#servericon - Аватар сервера.\n▫️#mes - Посмотреть сообщений пользователя.\n▫️#ping - Пинг бота.\n```', color = 0x00ff00)
        embed2 = discord.Embed(title="⚙️Навигация по командам:", description='📜Модерация:\n```\n▫️#clear - Очистить сообщения.\n▫️#delnote - Удалить заметку.\n▫️#note - Выдать заметку.\n▫️#delwarn - Удалить предупреждение.\n▫️#warn - Выдать предупреждение.\n▫️#ban - Забанить пользователя.\n▫️#kick - Кикнуть пользователя\n▫️#mute - Замьютить пользователя.\n▫️#unmute - Размьютить пользователя.\n▫️#warnings - Посмотреть предупреждения пользователя.\n▫️#notes - Посмотреть заметки пользователя.\n```', color = 0x00ff00)
        embed3 = discord.Embed(title="⚙️Навигация по командам:", description='<:cash:903999146569138216>Экономика:\n```\n▫️#bal - Посмотреть баланс пользователя.\n▫️#daily - Ежедневная награда.\n▫️#weekly - Еженедельная награда.\n▫️#dep - Положить деньги на банковский счёт.\n▫️#with - Снять деньги с банковского счёта.\n▫️#pay - Перевести деньги другому пользователю.\n▫️#roulette - Рулетка.\n▫️#add-money - Выдать деньги полльзователю.\n▫️#remove-money - Забрать деньги у пользователя.\n▫️#add-messages - Выдать сообщения пользователю.\n▫️#remove-messages - Забрать сообщения у пользователя.\n```', color = 0x00ff00)
        embeds = [embed1, embed2, embed3]
        message = await ctx.send(embed=embed1)
        page = Paginator(self.bot, message, only=ctx.author, use_more=False, embeds=embeds, footer=False, timeout=120)
        await page.start()

    @commands.command(aliases = ["add-role"])
    @commands.has_any_role(902849136041295883, 933769903910060153, 902841113734447214)
    async def addrole(self, ctx, member: discord.Member, role: discord.Role):
        embed = discord.Embed(
            description = f"Роль {role.mention} успешно выдана {member.mention}.",
            color = 0x00ff00
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        await member.add_roles(role)

        @addrole.error
        async def add_role_error(self, ctx, error):
            if isinstance(error, commands.errors.MissingRequiredArgument):
                embed = discord.Embed(
                    description = "<:noe:911292323365781515>Аргумент не указан.\n\nИспользование:\n`add-role <user> <role>`",
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

    @commands.command(aliases = ["remove-role"])
    @commands.has_any_role(902849136041295883, 933769903910060153, 902841113734447214)
    async def removerole(self, ctx, member: discord.Member, role: discord.Role):
        embed = discord.Embed(
            description = f"Роль {role.mention} успешно забрана у {member.mention}.",
            color = 0x00ff00
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        await member.remove_roles(role)

    @removerole.error
    async def remove_role_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Аргумент не указан.\n\nИспользование:\n`#remove-role <user> <role>`",
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

    @commands.command()
    @commands.has_any_role(902849136041295883, 933769903910060153, 902841113734447214)
    async def create(self, ctx, otvet, *, vopros):
        self.collserver.update_one(
            {
                "_id": ctx.guild.id
            },
            {
                "$push": {
                    "quiz": {
                        "answer": otvet.lower(),
                        "question":vopros
                    }
                }
            }
        )
        embed = discord.Embed(
            title = "Викторина",
            description = f"**Вопрос:** {vopros}",
            color = 0x00ff00
        )
        await self.bot.get_channel(938066272946622506).send(embed=embed)

    @commands.command()
    @commands.has_any_role(902849136041295883, 933769903910060153, 902841113734447214)
    async def delete(self, ctx, otvets):
        if self.collserver.count_documents({"quiz.answer": otvets}) == 0:
            await ctx.send("Даного ответа не найдено.")
        else:
            self.collserver.update_one(
                {
                    "quiz.answer": otvets
                },
                {
                    "$pull": {
                        "quiz": {
                            "answer": otvets
                        }
                    }
                }
            )
            embed = discord.Embed(
                description = f"<:check:930367892455850014>Ответ `{otvets}` был удалён.",
                color = 0x42aaff
            )
            await ctx.send(embed = embed)

    @commands.command()
    async def user(self, ctx, member: discord.Member = None):
        if member is None:
            date_format = "%a, %#d %B %Y, %I:%M %p"
            embed = discord.Embed(
                title = "Информация о пользователе:",
                color = 0x00ff00
            )
            embed.add_field(name="» Пользователь:", value=ctx.author, inline=False)
            embed.add_field(name="» Айди:", value=ctx.author.id, inline=False)
            stats = ctx.author.status
            if stats == discord.Status.online:
                embed.add_field(name="» Статус:", value="<:online:939411332799803432>В сети", inline=False)
            elif stats == discord.Status.offline:
                embed.add_field(name="» Статус:", value="<:offline:939411332602671115>Не в сети", inline=False)
            elif stats == discord.Status.dnd:
                embed.add_field(name="» Статус:", value="<:dnd:939411332254535731>Не беспокоить", inline=False)
            elif stats == discord.Status.idle:
                embed.add_field(name="» Статус:", value="<:idle:939411332850147368>Не активен", inline=False)
            embed.add_field(name="» Присоединился к серверу:", value=ctx.author.joined_at.strftime(date_format), inline=False)
            embed.add_field(name="» Аккаунт создан:", value=ctx.author.created_at.strftime(date_format), inline=False)
            icon = str(ctx.guild.icon_url)
            embed.set_thumbnail(url = icon)
            await ctx.send(embed = embed)
        else:
            date_format = "%a, %#d %B %Y, %I:%M %p"
            embed = discord.Embed(
                title = "Информация о пользователе:",
                color = 0x00ff00
            )
            embed.add_field(name="» Пользователь:", value=member, inline=False)
            embed.add_field(name="» Айди:", value=member.id, inline=False)
            stats = member.status
            if stats == discord.Status.online:
                embed.add_field(name="» Статус:", value="<:online:939411332799803432>В сети", inline=False)
            elif stats == discord.Status.offline:
                embed.add_field(name="» Статус:", value="<:offline:939411332602671115>Не в сети", inline=False)
            elif stats == discord.Status.dnd:
                embed.add_field(name="» Статус:", value="<:dnd:939411332254535731>Не беспокоить", inline=False)
            elif stats == discord.Status.idle:
                embed.add_field(name="» Статус:", value="<:idle:939411332850147368>Не активен", inline=False)
            embed.add_field(name="» Присоединился к серверу:", value=member.joined_at.strftime(date_format), inline=False)
            embed.add_field(name="» Аккаунт создан:", value=member.created_at.strftime(date_format), inline=False)
            icon = str(ctx.guild.icon_url)
            embed.set_thumbnail(url = icon)
            await ctx.send(embed = embed)

    @user.error
    async def user_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Аргумент не указан.\n\nИспользование:\n`#user <user>`",
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
