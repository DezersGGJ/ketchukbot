import discord
import random
import datetime
import humanize
import schedule
import time
import asyncio
from discord_components import DiscordComponents, Button, ButtonStyle, Select, SelectOption
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
    async def help(self, ctx):
        coin = self.bot.get_emoji(903999146569138216)
        embed = discord.Embed(title="Доступные команды:", color = 0x00ff00)
        embed.add_field(name="💎 Основные", value="`#avatar` `#servericon` `#mes` `#ping` `#shop` `#buy-shop`", inline=False)
        embed.add_field(name="🛡️ Модерирование", value="`#clear` `#delnote` `#note` `#delwarn` `#warn` `#ban` `#kick` `#mute` `#unmute` `#warnings` `#notes`", inline=False)
        embed.add_field(name="<:cash:903999146569138216> Экономические", value="`#bal` `#daily` `#weekly` `#deposit` `#withdraw` `#pay` `#roulette` `#add-money` `#remove-money` `#add-messages` `#remove-messages`", inline=False)
        embed.set_footer(text = 'Dezers', icon_url = "https://cdn.discordapp.com/avatars/810182387089932298/a_2bf1eab9a6b50fae544e22ba4442a43d.gif?size=1024")
        embed.set_thumbnail(url = "https://cdn.discordapp.com/avatars/840153710365376583/d419845380a3201bdd092cdefd281fda.webp?size=1024")
        await ctx.send(
            embed=embed,
            components=[
                Select(
                    placeholder="Выберите группу...",
                    options=[
                        SelectOption(label='Основные', value='e1', emoji='💎'),
                        SelectOption(label='Модерирование', value='e2', emoji='🛡️'),
                        SelectOption(label='Экономические', value='e3', emoji=coin),
                    ],
                    custom_id="help1",
                )
            ],
        )
        embed1 = discord.Embed(title="⚙️Навигация по командам:", color = 0x00ff00)
        embed2 = discord.Embed(title="Доступные команды группы **Модерирование** 🛡️", color = 0x00ff00)
        embed3 = discord.Embed(title="⚙️Навигация по командам:", color = 0x00ff00)
        embed2.add_field(name="#mute", value="Заглушить участника", inline=False)
        embed2.add_field(name="#unmute", value="Снять с участника мьют", inline=False)
        embed2.add_field(name="#ban", value="Заблокировать участника", inline=False)
        embed2.add_field(name="#kick", value="Изгнать участника", inline=False)
        embed2.add_field(name="#warn", value="Выдать предупреждение участнику", inline=False)
        embed2.add_field(name="#warnings", value="Показать список предупреждений", inline=False)
        embed2.add_field(name="#delwarn", value="Снять предупреждение участника", inline=False)
        embed2.add_field(name="#clear", value="Очистить сообщения", inline=False)
        embed2.add_field(name="#note", value="Выдать заметку участнику", inline=False)
        embed2.add_field(name="#delnote", value="Снять заметку участника", inline=False)
        embed2.add_field(name="#notes", value="Показать список заметок", inline=False)
        embed1.add_field(name="#avatar", value="Показать аватар участника", inline=False)
        embed1.add_field(name="#servericon", value="Снять аватар сервера", inline=False)
        embed1.add_field(name="#mes", value="Показать сообщения участника", inline=False)
        embed1.add_field(name="#ping", value="Показать задержку бота", inline=False)
        embed1.add_field(name="#shop", value="Показать список ролей в магазине", inline=False)
        embed1.add_field(name="#buy-shop", value="Купить роль в магазине", inline=False)
        embed3.add_field(name="#bal", value="Показать баланс пользователя", inline=False)
        embed3.add_field(name="#daily", value="Получить ежедневную награду", inline=False)
        embed3.add_field(name="#weekly", value="Получить еженедельную награду", inline=False)
        embed3.add_field(name="#deposit", value="Пополнить банковский счёт", inline=False)
        embed3.add_field(name="#withdraw", value="Снять деньги с банковского счёта", inline=False)
        embed3.add_field(name="#pay", value="Передать деньги участнику", inline=False)
        embed3.add_field(name="#roulette", value="Рулетка", inline=False)
        embed3.add_field(name="#add-money", value="Выдать деньги участнику", inline=False)
        embed3.add_field(name="#remove-money", value="Забрать деньги у участника", inline=False)
        embed3.add_field(name="#add-messages", value="Выдать сообщение участнику", inline=False)
        embed3.add_field(name="#remove-messages", value="Забрать сообщения у участника", inline=False)
        embed1.set_footer(text = 'Dezers', icon_url = "https://cdn.discordapp.com/avatars/810182387089932298/a_2bf1eab9a6b50fae544e22ba4442a43d.gif?size=1024")
        embed1.set_thumbnail(url = "https://cdn.discordapp.com/avatars/840153710365376583/d419845380a3201bdd092cdefd281fda.webp?size=1024")
        embed2.set_footer(text = 'Dezers', icon_url = "https://cdn.discordapp.com/avatars/810182387089932298/a_2bf1eab9a6b50fae544e22ba4442a43d.gif?size=1024")
        embed2.set_thumbnail(url = "https://cdn.discordapp.com/avatars/840153710365376583/d419845380a3201bdd092cdefd281fda.webp?size=1024")
        embed3.set_footer(text = 'Dezers', icon_url = "https://cdn.discordapp.com/avatars/810182387089932298/a_2bf1eab9a6b50fae544e22ba4442a43d.gif?size=1024")
        embed3.set_thumbnail(url = "https://cdn.discordapp.com/avatars/840153710365376583/d419845380a3201bdd092cdefd281fda.webp?size=1024")
        deadline = time.monotonic() + 60
        while time.monotonic() < deadline:
            interaction = await self.bot.wait_for("select_option", check=lambda inter: inter.custom_id == "help1" and inter.user == ctx.author)
            res = interaction.values[0]
            if res == "e1":
                await interaction.respond(embed=embed1)
            elif res == "e2":
                await interaction.respond(embed=embed2)
            elif res == "e3":
                await interaction.respond(embed=embed3)

    @commands.command()
    async def avatar(self, ctx, *, member: discord.Member=None):
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
    async def messages(self, ctx, *, member: discord.Member = None):
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

    @commands.command(aliases=["add-shop"])
    @commands.has_any_role(902849136041295883, 902841113734447214, 933769903910060153)
    async def add_shop(self, ctx, role: discord.Role = None, cost: int = None, *, desc = "Нету"):
        if role is None:
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Укажите роль которую хотите добавить в магазин.",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            if cost is None:
                embed = discord.Embed(
                    description = "<:noe:911292323365781515>Укажите стоимость роли которую хотите добавить в магазин.",
                    color = 0xff2400
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
            elif cost < 0:
                embed = discord.Embed(
                    description = "<:noe:911292323365781515>Введите сумму больше <:cash:903999146569138216>0.",
                    color = 0xff2400
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
            else:
                self.collserver.update_one(
                    {
                        "_id": ctx.guild.id
                    },
                    {
                        "$push": {
                            "roleshop": {
                                "roleid": role.id,
                                "rolename": role.name,
                                "desc": desc,
                                "cost": cost,
                            }
                        }
                    }
                )
                await ctx.message.add_reaction('<:check:930367892455850014>')

    @commands.command()
    async def shop(self, ctx):
        guild = self.collserver.find_one({"_id": ctx.guild.id})
        embed = discord.Embed(description = "Купите роль с помощью команды: `buy-shop <role name or id>`.", color = 0x03a8f4)
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        i = 1
        for value in guild["roleshop"]:
            embed.add_field(name=f"{i}. {value['rolename']} - <:cash:903999146569138216>{humanize.intcomma(value['cost'])}", value=f"{value['desc']}", inline=False)
            i += 1
        await ctx.send(embed=embed)

    @commands.command(aliases=["delete-shop"])
    @commands.has_any_role(902849136041295883, 902841113734447214, 933769903910060153)
    async def delete_shop(self, ctx, *, role: discord.Role = None):
        if role is None:
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Укажите номер роли которую хотите удалить с магазина.",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            if self.collserver.count_documents({"roleshop.roleid": role.id}) == 0:
                await ctx.send("Даной роли не найдено.")
            else:
                self.collserver.update_one(
                    {
                        "roleshop.roleid": role.id
                    },
                    {
                        "$pull": {
                            "roleshop": {
                                "roleid": role.id
                            }
                        }
                    }
                )
                embed = discord.Embed(
                    description = "<:check:930367892455850014>Вы успешно удалили указанную роль.",
                    color = 0x42aaff
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)

    @commands.command(aliases=["buy-shop"])
    async def buy(self, ctx, *, role: discord.Role = None):
        if role is None:
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Укажите роль, которую вы желаете приобрести.",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            if role in ctx.author.roles:
                embed = discord.Embed(
                    description = "<:noe:911292323365781515>У вас уже имеется данная роль.",
                    color = 0xff2400
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
            else:
                if self.collserver.count_documents({"roleshop.roleid": role.id}) == 0:
                    embed = discord.Embed(
                        description = "<:noe:911292323365781515>Данной роли нет в магазине.",
                        color = 0xff2400
                    )
                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                else:
                    guild = self.collserver.find_one({"_id": ctx.guild.id})
                    for value in guild['roleshop']:
                        if value['roleid'] == role.id:
                            if value['cost'] > self.collection.find_one({"_id": ctx.author.id})['money']:
                                embed = discord.Embed(
                                    description = f"<:noe:911292323365781515>У вас недостаточно средств.",
                                    color = 0xff2400
                                )
                                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                await ctx.send(embed = embed)
                            else:
                                embed = discord.Embed(
                                    description = f"<:check:930367892455850014>Вы купили <@&{value['roleid']}> за <:cash:903999146569138216>{humanize.intcomma(value['cost'])}.",
                                    color = 0x00ff00
                                )
                                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                self.collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": -value['cost']}})
                                await ctx.author.add_roles(role)
                                await ctx.send(embed=embed)
                        else:
                            embed = discord.Embed(
                                description = f"<:noe:911292323365781515>Данной роли нет в магазине.",
                                color = 0xff2400
                            )
                            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                            await ctx.send(embed = embed)



def setup(bot):
    bot.add_cog(Basic(bot))
