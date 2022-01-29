import discord
import random
import datetime
import humanize
from discord.ext import commands
from pymongo import MongoClient

class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.cluster = MongoClient("mongodb+srv://DezersGG:Weerweer333@cluster0.b9xjp.mongodb.net/ecodb?retryWrites=true&w=majority")
        self.collection = self.cluster.ecodb.colldb
        self.collserver = self.cluster.ecodb.collserver

    @commands.command(aliases = ["purge"])
    @commands.has_any_role(902849136041295883, 506864696562024448, 902841113734447214, 903384312303472660, 903646061804023808, 903384319937085461, 933769903910060153)
    async def clear(self, ctx, amount: int):
        if amount > 0:
            if amount < 200:
                number = amount + 1
                await ctx.channel.purge(limit=number)
                await ctx.send(f"<:check:930367892455850014>Удалено {amount} сообщений.")

    @commands.command(aliases = ["remove-note"])
    @commands.has_any_role(902849136041295883, 506864696562024448, 902841113734447214, 903384312303472660, 903646061804023808, 933769903910060153)
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
                    embed.add_field(name = f"`Заметка #{value['note']}` <t:{value['time']}:f> {bot.get_user(value['author_id'])}", value = f"**Заметка:** {value['reason_note']}", inline = False)

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
                    embed.add_field(name = f"`Заметка #{value['note']}` <t:{value['time']}:f> {bot.get_user(value['author_id'])}", value = f"**Заметка:** {value['reason_note']}", inline = False)

                await ctx.send(embed = embed)

        @commands.command()
        @commands.has_any_role(902849136041295883, 506864696562024448, 902841113734447214, 903384312303472660, 903646061804023808, 933769903910060153)
        async def note(self, ctx, member: discord.Member, *, reason_note = "Нету"):
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

    @commands.command(aliases = ["remove-warn"])
    @commands.has_any_role(902849136041295883, 506864696562024448, 902841113734447214, 903384312303472660, 903646061804023808, 903384319937085461, 933769903910060153)
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

    @commands.command()
    @commands.has_any_role(902849136041295883, 506864696562024448, 902841113734447214, 903384312303472660, 903646061804023808, 903384319937085461, 933769903910060153)
    async def warn(self, ctx, member: discord.Member, *, reason = "Нету"):
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


def setup(bot):
    bot.add_cog(Moderation(bot))
