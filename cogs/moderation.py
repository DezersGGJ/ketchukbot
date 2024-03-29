import discord
import random
import datetime
import humanize
from discord.ext import commands, tasks
from pymongo import MongoClient
from func import *

class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.cluster = MongoClient("mongodb+srv://DezersGG:Weerweer333@cluster0.b9xjp.mongodb.net/ecodb?retryWrites=true&w=majority")
        self.collection = self.cluster.ecodb.colldb
        self.collserver = self.cluster.ecodb.collserver

    @tasks.loop(minutes=1.0)
    async def colorit(self):
        server = self.bot.get_guild(id=902831072247709757)
        role = server.get_role(944888747818901534)
        colors = ['0xFF0000', '0xFFA500', '0xFFFF00', '0x008000', '0x0000FF', '0x800080']
        await role.edit(color=random.choice(colors))

    @tasks.loop()
    async def check_mutes(self):
        current = datetime.datetime.now()
        mutes = load_json("jsons/mutes.json")
        users, times = list(mutes.keys()), list(mutes.values())
        for i in range(len(times)):
            time = times[i]
            unmute = datetime.datetime.strptime(str(time), "%c")
            if unmute < current:
                user_id = users[times.index(time)]
                try:
                    member = await self.guild.fetch_member(int(user_id))
                    await member.remove_roles(self.mutedrole)
                    mutes.pop(str(member.id))
                except discord.NotFound:
                    pass
                write_json("jsons/mutes.json", mutes)

    @commands.command(aliases = ["purge"])
    @commands.has_any_role(902849136041295883, 933769903910060153, 902841113734447214, 903384312303472660, 903646061804023808, 903384319937085461)
    async def clear(self, ctx, amount: int):
        if amount > 0:
            if amount < 200:
                number = amount + 1
                await ctx.channel.purge(limit=number)
                await ctx.send(f"<:check:930367892455850014>Удалено {amount} сообщений.", delete_after=5)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Аргумент не указан.\n\nИспользование:\n`#clear <amount>`",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.errors.BadArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Неправильно указан аргумент `<amount>`.\n\nИспользование:\n`#clear <amount>`",
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

    @commands.command(aliases = ["remove-note"])
    @commands.has_any_role(902849136041295883, 933769903910060153, 902841113734447214, 903384312303472660, 903646061804023808)
    async def delnote(self, ctx, note: int):
        if self.collection.count_documents({"notes.note": note}) == 0:
            await ctx.send("Данной заметки не найдено.")
        else:
            self.collection.update_one(
                {
                    "notes.note": note
                },
                {
                    "$inc": {
                        "note": -1
                    },
                    "$pull": {
                        "notes": {
                            "note": note
                        }
                    }
                }
            )
            embed = discord.Embed(
                description = f"<:check:930367892455850014>Заметка `#{note}` была удалена.",
                color = 0x42aaff
            )
            await ctx.send(embed = embed)

    @delnote.error
    async def delnote_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Аргумент не указан.\n\nИспользование:\n`#delnote <note>`",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.errors.BadArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Неправильно указан аргумент `<note>`.\n\nИспользование:\n`#delnote <note>`",
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
    async def notes(self, ctx, member: discord.Member = None):
        if member is None:
            if self.collection.find_one({"_id": ctx.author.id})["note"] == 0:
                embed = discord.Embed(
                    title = f"Заметки участника {ctx.author.name}:",
                    description = "Заметки отсутствуют.",
                    color = 0x42aaff
                )
                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(title = f"Заметки участника {ctx.author.name}:", color = 0x42aaff)
                user = self.collection.find_one({"_id": ctx.author.id})
                for value in user["notes"]:
                    embed.add_field(name = f"`Заметка #{value['note']}` <t:{value['time']}:f> {self.bot.get_user(value['author_id'])}", value = f"**Заметка:** {value['reason_note']}", inline = False)

                await ctx.send(embed = embed)
        else:
            if self.collection.find_one({"_id": member.id})["note"] == 0:
                embed = discord.Embed(
                    title = f"Заметки участника {member.name}:",
                    description = "Заметки отсутствуют.",
                    color = 0x42aaff
                )
                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(title = f"Заметки участника {member.name}:", color = 0x42aaff)
                user = self.collection.find_one({"_id": member.id})
                for value in user["notes"]:
                    embed.add_field(name = f"`Заметка #{value['note']}` <t:{value['time']}:f> {self.bot.get_user(value['author_id'])}", value = f"**Заметка:** {value['reason_note']}", inline = False)

                await ctx.send(embed = embed)

    @notes.error
    async def notes_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Аргумент не указан.\n\nИспользование:\n`#notes <user>`",
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
    @commands.has_any_role(902849136041295883, 933769903910060153, 902841113734447214, 903384312303472660, 903646061804023808)
    async def note(self, ctx, member: discord.Member, *, reason_note = "Не указана"):
        self.collserver.update_one(
            {
                "_id": ctx.guild.id
            },
            {
                "$inc": {
                    "note": 1
                }
            }
        )
        timenote = int(datetime.datetime.utcnow().timestamp())
        self.collection.update_one(
            {
                "_id": member.id
            },
            {
                "$push": {
                    "notes": {
                        "author_id": ctx.author.id,
                        "reason_note": reason_note,
                        "time": timenote,
                        "note": self.collserver.find_one({"_id": ctx.guild.id})["note"]
                    }
                },
                "$inc": {
                    "note": 1
                }
            }
        )
        embed = discord.Embed(
            description = f"Пользователю {member} была выдана заметка.",
            color = 0x42aaff
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed = embed)

    @note.error
    async def note_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Аргумент не указан.\n\nИспользование:\n`#note <user> <reason>`",
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

    @commands.command(aliases = ["remove-warn"])
    @commands.has_any_role(902849136041295883, 933769903910060153, 902841113734447214, 903384312303472660, 903646061804023808, 903384319937085461)
    async def delwarn(self, ctx, case: int):
        if self.collection.count_documents({"reasons.case": case}) == 0:
            await ctx.send("Даного случая не найдено.")
        else:
            self.collection.update_one(
                {
                    "reasons.case": case
                },
                {
                    "$inc": {
                        "warns": -1
                    },
                    "$pull": {
                        "reasons": {
                            "case": case
                        }
                    }
                }
            )
            embed = discord.Embed(
                description = f"<:check:930367892455850014>Предупреждение `#{case}` было снято.",
                color = 0x42aaff
            )
            await ctx.send(embed = embed)

    @delwarn.error
    async def delwarn_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Аргумент не указан.\n\nИспользование:\n`#delwarn <case>`",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.errors.BadArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Неправильно указан аргумент `<note>`.\n\nИспользование:\n`#delwarn <case>`",
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

    @commands.command(aliases = ["warnings"])
    async def infractions(self, ctx, member: discord.Member = None):
        if member is None:
            if self.collection.find_one({"_id": ctx.author.id})["warns"] == 0:
                embed = discord.Embed(
                    title = f"Предупреждения участника {ctx.author.name}:",
                    description = "Предупреждения отсутствуют.",
                    color = 0x42aaff
                )
                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(title = f"Предупреждения участника {ctx.author.name}:", color = 0x42aaff)
                user = self.collection.find_one({"_id": ctx.author.id})
                for value in user["reasons"]:
                    embed.add_field(name = f"`Случай #{value['case']}` <t:{value['time']}:f> {self.bot.get_user(value['author_id'])}", value = f"**Причина:** {value['reason']}", inline = False)

                await ctx.send(embed = embed)
        else:
            if self.collection.find_one({"_id": member.id})["warns"] == 0:
                embed = discord.Embed(
                    title = f"Предупреждения участника {member.name}:",
                    description = "Предупреждения отсутствуют.",
                    color = 0x42aaff
                )
                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(title = f"Предупреждения участника {member.name}:", color = 0x42aaff)
                user = self.collection.find_one({"_id": member.id})
                for value in user["reasons"]:
                    embed.add_field(name = f"`Случай #{value['case']}` <t:{value['time']}:f> {self.bot.get_user(value['author_id'])}", value = f"**Причина:** {value['reason']}", inline = False)

                await ctx.send(embed = embed)

    @infractions.error
    async def infractions_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Аргумент не указан.\n\nИспользование:\n`#infractions <user>`",
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
    @commands.has_any_role(902849136041295883, 933769903910060153, 902841113734447214, 903384312303472660, 903646061804023808, 903384319937085461)
    async def warn(self, ctx, member: discord.Member, *, reason = "Не указана"):
        self.collserver.update_one(
            {
                "_id": ctx.guild.id
            },
            {
                "$inc": {
                    "case": 1
                }
            }
        )
        timewarn = int(datetime.datetime.utcnow().timestamp())
        self.collection.update_one(
            {
                "_id": member.id
            },
            {
                "$inc": {
                    "warns": 1
                },
                "$push": {
                    "reasons": {
                        "author_id": ctx.author.id,
                        "reason": reason,
                        "time": timewarn,
                        "case": self.collserver.find_one({"_id": ctx.guild.id})["case"]
                    }
                }
            }
        )
        embed = discord.Embed(
            description = f"Пользователю {member} было выдано предупреждение.\nПричина: {reason}",
            color = 0x42aaff
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed = embed)

    @warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Аргумент не указан.\n\nИспользование:\n`#warn <user> <reason>`",
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
    @commands.has_any_role(902849136041295883, 933769903910060153, 902841113734447214, 903384312303472660, 903646061804023808)
    async def ban(self, ctx, member: discord.Member, *, reason="Не указана"):
        if member != ctx.author:
            if member.bot is False:
                rolelist = [902849136041295883, 933769903910060153, 902841113734447214, 903384312303472660, 903646061804023808, 903384319937085461]
                if any(role.id in rolelist for role in member.roles):
                    embed = discord.Embed(
                        description = "<:noe:911292323365781515>Вы не можете применить эту команду к себе, другому модератору или боту.",
                        color = 0xff2400
                    )
                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(
                        description = f"Участник **{member.name}** был забанен.",
                        color = 0x00ff00
                    )
                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    await member.ban(reason=reason)
                    await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    description = "<:noe:911292323365781515>Вы не можете применить эту команду к себе, другому модератору или боту.",
                    color = 0xff2400
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Вы не можете применить эту команду к себе, другому модератору или боту.",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Аргумент не указан.\n\nИспользование:\n`#ban <user> <reason>`",
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
    @commands.has_any_role(902849136041295883, 933769903910060153, 902841113734447214, 903384312303472660, 903646061804023808)
    async def kick(self, ctx, member: discord.Member, *, reason="Не указана"):
        if member != ctx.author:
            if member.bot is False:
                rolelist = [902849136041295883, 933769903910060153, 902841113734447214, 903384312303472660, 903646061804023808, 903384319937085461]
                if any(role.id in rolelist for role in member.roles):
                    embed = discord.Embed(
                        description = "<:noe:911292323365781515>Вы не можете применить эту команду к себе, другому модератору или боту.",
                        color = 0xff2400
                    )
                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(
                        description = f"Участник **{member.name}** был выгнан.",
                        color = 0x00ff00
                    )
                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    await member.kick(reason=reason)
                    await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    description = "<:noe:911292323365781515>Вы не можете применить эту команду к себе, другому модератору или боту.",
                    color = 0xff2400
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Вы не можете применить эту команду к себе, другому модератору или боту.",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Аргумент не указан.\n\nИспользование:\n`#kick <user> <reason>`",
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
    @commands.has_any_role(902849136041295883, 933769903910060153, 902841113734447214, 903384312303472660, 903646061804023808, 903384319937085461)
    async def mute(self, ctx, member: discord.Member, time: str = None, *, reason="Не указана"):
        rolelist = [902849136041295883, 933769903910060153, 902841113734447214, 903384312303472660, 903646061804023808, 903384319937085461]
        if member.bot is True:
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Вы не можете применить эту команду к себе, другому модератору или боту.",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        if member == ctx.author:
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Вы не можете применить эту команду к себе, другому модератору или боту.",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        if len(reason) > 150:
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Причина не может быть больше 150 символов.",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        if time is None:
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Вы не указали длительность.",
                color = 0xff2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            if any(role.id in rolelist for role in member.roles):
                embed = discord.Embed(
                    description = "<:noe:911292323365781515>Вы не можете применить эту команду к себе, другому модератору или боту.",
                    color = 0xff2400
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
            else:
                try:
                    seconds = int(time[:-1])
                    duration = time[-1]
                    if duration == "s":
                        pass
                    if duration == "m":
                        seconds *= 60
                    if duration == "h":
                        seconds *= 3600
                    if duration == "d":
                        seconds *= 86400
                    if duration == "w":
                        seconds *= 604800
                except:
                    embed = discord.Embed(
                        description = "<:noe:911292323365781515>Указана неправильная длительность.",
                        color = 0xff2400
                    )
                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                mute_expiration = (datetime.datetime.now() + datetime.timedelta(seconds=int(seconds))).strftime("%c")
                role = self.mutedrole
                if not role:
                    embed = discord.Embed(
                        description = "<:noe:911292323365781515>Роль мута не найдена.",
                        color = 0xff2400
                    )
                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                mutes = load_json("jsons/mutes.json")
                try:
                    member_mute = mutes[str(member.id)]
                    embed = discord.Embed(
                        description = "<:noe:911292323365781515>Пользователь уже в муте.",
                        color = 0xff2400
                    )
                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                except:
                    mutes[str(member.id)] = str(mute_expiration)
                    write_json("jsons/mutes.json", mutes)
                    timemute = datetime.timedelta(seconds=int(seconds))
                    embed = discord.Embed(
                        description = f"Участник **{member.name}** был замьючен.\n**Модератор:**\n{ctx.author}\n**Срок:**\n{time}\n**Причина:**\n{reason}",
                        color = 0x00ff00
                    )
                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    await member.add_roles(role)
                    await member.move_to(channel=None)
                    await ctx.send(embed=embed)

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Аргумент не указан.\n\nИспользование:\n`#mute <user> <time> <reason>`",
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
    @commands.has_any_role(902849136041295883, 933769903910060153, 902841113734447214, 903384312303472660, 903646061804023808, 903384319937085461)
    async def unmute(self, ctx, member: discord.Member):
        embed = discord.Embed(
            description = f"Участник **{member.name}** был размьючен.\n**Модератор**\n{ctx.author}",
            color = 0x00ff00
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        await member.remove_roles(self.mutedrole)
        mutes = load_json("jsons/mutes.json")
        mutes.pop(str(member.id))
        write_json("jsons/mutes.json", mutes)

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(
                description = "<:noe:911292323365781515>Аргумент не указан.\n\nИспользование:\n`#unmute <user>`",
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

    @commands.Cog.listener()
    async def on_ready(self):
        self.guild = await self.bot.fetch_guild(902831072247709757)
        self.mutedrole = discord.utils.get(self.guild.roles, id=906283550641365005)
        self.check_mutes.start()


def setup(bot):
    bot.add_cog(Moderation(bot))
