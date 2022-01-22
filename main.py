#biblites
import discord
import datetime
import random
import json
import requests
import os
import asyncio
from discord.ext import commands
from pymongo import MongoClient
from Cybernator import Paginator
from discord_components import DiscordComponents, Button, ButtonStyle, Select, SelectOption
import humanize


bot = commands.Bot(command_prefix = '#', intents = discord.Intents.all())
bot.remove_command('help')
cluster = MongoClient("mongodb+srv://DezersGG:Weerweer333@cluster0.b9xjp.mongodb.net/ecodb?retryWrites=true&w=majority")
collection = cluster.ecodb.colldb
collserver = cluster.ecodb.collserver
#umoney = collection.find_one({"_id": ctx.author.id})["money"]
#collection.update_one({"_id": ctx.author.id}, {"$set": {"money": umoney + amount}})
#event
@bot.event
async def on_ready():
    print("Bot connected to the server")
    DiscordComponents(bot)
    await bot.change_presence(status = discord.Status.online, activity = discord.Game('Бот в разработке.'))
    for guild in bot.guilds:
        for member in guild.members:
            user = {
                "_id": member.id,
                "money": 0,
                "mes": 0,
                "bank": 0,
                "cddaily": 0,
                "cdweekly": 0,
                "cdwork": 0,
                "warns": 0,
                "reasons": [],
                "notes": [],
                "note": 0,
                "mute": []
            }
            server = {
                "_id": guild.id,
                "case": 0,
                "note": 0
            }

            if collection.count_documents({"_id": member.id}) == 0:
                collection.insert_one(user)
            if collserver.count_documents({"_id": guild.id}) == 0:
                collserver.insert_one(server)

@bot.event
async def on_member_join(member):
    if member.bot == False:
      embed = discord.Embed(
          description = f"Участник **{member.name}** присоединился к серверу.",
          color = 0x42aaff
      )
      icon = str(member.guild.icon_url)
      embed.set_thumbnail(url = icon)
      await bot.get_channel(903710414783791114).send(embed=embed)

    user = {
        "_id": member.id,
        "money": 0,
        "mes": 0,
        "bank": 0,
        "cddaily": 0,
        "cdweekly": 0,
        "cdwork": 0,
        "warns": 0,
        "reasons": [],
        "notes": [],
        "note": 0,
        "mute": []
    }

    if collection.count_documents({"_id": member.id}) == 0:
        collection.insert_one(user)

@bot.event
async def on_message_delete(message):
    if message.author.bot == False:
      embed = discord.Embed(
          title = "Сообщение было удалено",
          description = f"**Удалённое сообщение:**\n{message.content}\n**Автор:**\n{message.author.mention}\n**Канал:**\n{message.channel.mention}",
          color = 0x42aaff
      )
      await bot.get_channel(903710414783791114).send(embed=embed)


@bot.event
async def on_member_remove(member):
    if member.bot == False:
      embed = discord.Embed(
          description = f"Участник **{member.name}** вышел с сервера.",
          color = 0x42aaff
      )
      icon = str(member.guild.icon_url)
      embed.set_thumbnail(url = icon)
      await bot.get_channel(903710414783791114).send(embed=embed)


@bot.event
async def on_message_edit(before, after):
    if before.author.bot == False:
      embed = discord.Embed(
          title = "Сообщение было отредоктировано",
          description = f"**Старое содержимое:**\n{before.content}\n**Новое содиржимое:**\n{after.content}\n**Автор:**\n{before.author.mention}\n**Канал:**\n{before.channel.mention}",
          color = 0x42aaff
      )
      await bot.get_channel(903710414783791114).send(embed=embed)


@bot.event
async def on_message(message):
    if message.author.bot == False:
        if message.channel.id == 902855972509327400:
            umes = collection.find_one({"_id": message.author.id})["mes"]
            collection.update_one({"_id": message.author.id}, {"$set": {"mes": umes + 1}})
            if umes == 149:
                umes = collection.find_one({"_id": message.author.id})["mes"]
                umoney = collection.find_one({"_id": message.author.id})["money"]
                guild = bot.get_guild(message.guild.id)
                role_id = guild.get_role(903385564781350962)
                await message.author.add_roles(role_id)
                collection.update_one({"_id": message.author.id}, {"$set": {"money": umoney + 15000}})
            elif umes == 299:
                umes = collection.find_one({"_id": message.author.id})["mes"]
                umoney = collection.find_one({"_id": message.author.id})["money"]
                guild = bot.get_guild(message.guild.id)
                role_id = guild.get_role(905008758277681153)
                await message.author.add_roles(role_id)
                collection.update_one({"_id": message.author.id}, {"$set": {"money": umoney + 30000}})
            elif umes == 499:
                umes = collection.find_one({"_id": message.author.id})["mes"]
                umoney = collection.find_one({"_id": message.author.id})["money"]
                guild = bot.get_guild(message.guild.id)
                role_id = guild.get_role(904708571156066314)
                await message.author.add_roles(role_id)
                collection.update_one({"_id": message.author.id}, {"$set": {"money": umoney + 50000}})
            elif umes == 999:
                umes = collection.find_one({"_id": message.author.id})["mes"]
                umoney = collection.find_one({"_id": message.author.id})["money"]
                guild = bot.get_guild(message.guild.id)
                role_id = guild.get_role(904712301255467058)
                await message.author.add_roles(role_id)
                collection.update_one({"_id": message.author.id}, {"$set": {"money": umoney + 100000}})
            elif umes == 1749:
                umes = collection.find_one({"_id": message.author.id})["mes"]
                umoney = collection.find_one({"_id": message.author.id})["money"]
                guild = bot.get_guild(message.guild.id)
                role_id = guild.get_role(904714252089188382)
                await message.author.add_roles(role_id)
                collection.update_one({"_id": message.author.id}, {"$set": {"money": umoney + 175000}})
            elif umes == 2999:
                umes = collection.find_one({"_id": message.author.id})["mes"]
                umoney = collection.find_one({"_id": message.author.id})["money"]
                guild = bot.get_guild(message.guild.id)
                role_id = guild.get_role(904714499804790786)
                await message.author.add_roles(role_id)
                collection.update_one({"_id": message.author.id}, {"$set": {"money": umoney + 300000}})
            elif umes == 4999:
                umes = collection.find_one({"_id": message.author.id})["mes"]
                umoney = collection.find_one({"_id": message.author.id})["money"]
                guild = bot.get_guild(message.guild.id)
                role_id = guild.get_role(904715362715721769)
                await message.author.add_roles(role_id)
                collection.update_one({"_id": message.author.id}, {"$set": {"money": umoney + 500000}})
            elif umes > 5000:
                umoney = collection.find_one({"_id": message.author.id})["money"]
                collection.update_one({"_id": message.author.id}, {"$set": {"money": umoney + 100}})

    await bot.process_commands(message)

#economy
@bot.command()
async def daily(ctx):
    if collection.find_one({'_id': ctx.author.id})['cddaily'] == 0:
        amount = random.randint(2000,5000)
        umoney = collection.find_one({"_id": ctx.author.id})["money"]
        time = int(datetime.datetime.utcnow().timestamp())
        collection.update_one({"_id": ctx.author.id}, {"$set": {"cddaily": time}})
        collection.update_one({"_id": ctx.author.id}, {"$set": {"money": umoney + amount}})
        embed = discord.Embed(
            description = f"Твоя ежедневная награда составила <:cash:903999146569138216>{amount}.",
            color = 0x00ff00
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed = embed)
    else:
        time = collection.find_one({"_id": ctx.author.id})["cddaily"]
        cdtime = int(datetime.datetime.utcnow().timestamp()) - 86400
        if time < cdtime:
            amount = random.randint(2000,5000)
            umoney = collection.find_one({"_id": ctx.author.id})["money"]
            time = int(datetime.datetime.utcnow().timestamp())
            collection.update_one({"_id": ctx.author.id}, {"$set": {"cddaily": time}})
            collection.update_one({"_id": ctx.author.id}, {"$set": {"money": umoney + amount}})
            embed = discord.Embed(
                description = f"Твоя ежедневная награда составила <:cash:903999146569138216>{amount}.",
                color = 0x00ff00
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        else:
            cdtime = int(datetime.datetime.utcnow().timestamp()) - 86400
            time = collection.find_one({"_id": ctx.author.id})["cddaily"] - cdtime
            cooldown = str(datetime.timedelta(seconds=time))
            embed = discord.Embed(
                description = f"<:timecooldown:911306427723841566>Вы сможете получить ежедневную награду через {cooldown}",
                color = 0xFF2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)


@bot.command()
async def weekly(ctx):
    if collection.find_one({'_id': ctx.author.id})['cdweekly'] == 0:
        amount = random.randint(5000,20000)
        umoney = collection.find_one({"_id": ctx.author.id})["money"]
        time = int(datetime.datetime.utcnow().timestamp())
        collection.update_one({"_id": ctx.author.id}, {"$set": {"cdweekly": time}})
        collection.update_one({"_id": ctx.author.id}, {"$set": {"money": umoney + amount}})
        embed = discord.Embed(
            description = f"Твоя еженедельная награда составила <:cash:903999146569138216>{amount}.",
            color = 0x00ff00
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed = embed)
    else:
        time = collection.find_one({"_id": ctx.author.id})["cdweekly"]
        cdtime = int(datetime.datetime.utcnow().timestamp()) - 604800
        if time < cdtime:
            amount = random.randint(5000,20000)
            umoney = collection.find_one({"_id": ctx.author.id})["money"]
            time = int(datetime.datetime.utcnow().timestamp())
            collection.update_one({"_id": ctx.author.id}, {"$set": {"cdweekly": time}})
            collection.update_one({"_id": ctx.author.id}, {"$set": {"money": umoney + amount}})
            embed = discord.Embed(
                description = f"Твоя еженедельная награда составила <:cash:903999146569138216>{amount}.",
                color = 0x00ff00
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        else:
            cdtime = int(datetime.datetime.utcnow().timestamp()) - 604800
            time = collection.find_one({"_id": ctx.author.id})["cdweekly"] - cdtime
            cooldown = str(datetime.timedelta(seconds=time))
            embed = discord.Embed(
                description = f"<:timecooldown:911306427723841566>Вы сможете получить еженедельную награду через {cooldown}",
                color = 0xFF2400
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)


@bot.command(aliases = ["mes"])
async def messages(ctx, member: discord.Member = None):
    if member is None:
        umes = collection.find_one({"_id": ctx.author.id})["mes"]
        if umes < 149:
            embed = discord.Embed(
                description = f"{ctx.author} имеет `{collection.find_one({'_id': ctx.author.id})['mes']}` сообщений. `{150 - umes}` нужно для получения <@&903385564781350962>",
                color = 0x00ff00
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        elif umes < 299:
            embed = discord.Embed(
                description = f"{ctx.author} имеет `{collection.find_one({'_id': ctx.author.id})['mes']}` сообщений. `{300 - umes}` нужно для получения <@&905008758277681153>",
                color = 0x00ff00
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        elif umes < 499:
            embed = discord.Embed(
                description = f"{ctx.author} имеет `{collection.find_one({'_id': ctx.author.id})['mes']}` сообщений. `{500 - umes}` нужно для получения <@&904708571156066314>",
                color = 0x00ff00
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        elif umes < 999:
            embed = discord.Embed(
                description = f"{ctx.author} имеет `{collection.find_one({'_id': ctx.author.id})['mes']}` сообщений. `{1000 - umes}` нужно для получения <@&904712301255467058>",
                color = 0x00ff00
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        elif umes < 1749:
            embed = discord.Embed(
                description = f"{ctx.author} имеет `{collection.find_one({'_id': ctx.author.id})['mes']}` сообщений. `{1750 - umes}` нужно для получения <@&904714252089188382>",
                color = 0x00ff00
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        elif umes < 2999:
            embed = discord.Embed(
                description = f"{ctx.author} имеет `{collection.find_one({'_id': ctx.author.id})['mes']}` сообщений. `{3000 - umes}` нужно для получения <@&904714499804790786>",
                color = 0x00ff00
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        elif umes < 4999:
            embed = discord.Embed(
                description = f"{ctx.author} имеет `{collection.find_one({'_id': ctx.author.id})['mes']}` сообщений. `{5000 - umes}` нужно для получения <@&904715362715721769>",
                color = 0x00ff00
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        elif umes > 4999:
            embed = discord.Embed(
                description = f"{ctx.author} имеет `{collection.find_one({'_id': ctx.author.id})['mes']}` сообщений.",
                color = 0x00ff00
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)

    else:
        mmes = collection.find_one({"_id": member.id})["mes"]
        if mmes < 149:
            embed = discord.Embed(
                description = f"{member} имеет `{collection.find_one({'_id': member.id})['mes']}` сообщений. `{150 - mmes}` нужно для получения <@&903385564781350962>",
                color = 0x00ff00
            )
            embed.set_author(name=member, icon_url=member.avatar_url)
            await ctx.send(embed = embed)
        elif mmes < 299:
            embed = discord.Embed(
                description = f"{member} имеет `{collection.find_one({'_id': member.id})['mes']}` сообщений. `{300 - mmes}` нужно для получения <@&905008758277681153>",
                color = 0x00ff00
            )
            embed.set_author(name=member, icon_url=member.avatar_url)
            await ctx.send(embed = embed)
        elif mmes < 499:
            embed = discord.Embed(
                description = f"{member} имеет `{collection.find_one({'_id': member.id})['mes']}` сообщений. `{500 - mmes}` нужно для получения <@&904708571156066314>",
                color = 0x00ff00
            )
            embed.set_author(name=member, icon_url=member.avatar_url)
            await ctx.send(embed = embed)
        elif mmes < 999:
            embed = discord.Embed(
                description = f"{member} имеет `{collection.find_one({'_id': member.id})['mes']}` сообщений. `{1000 - mmes}` нужно для получения <@&904712301255467058>",
                color = 0x00ff00
            )
            embed.set_author(name=member, icon_url=member.avatar_url)
            await ctx.send(embed = embed)
        elif mmes < 1749:
            embed = discord.Embed(
                description = f"{member} имеет `{collection.find_one({'_id': member.id})['mes']}` сообщений. `{1750 - mmes}` нужно для получения <@&904714252089188382>",
                color = 0x00ff00
            )
            embed.set_author(name=member, icon_url=member.avatar_url)
            await ctx.send(embed = embed)
        elif mmes < 2999:
            embed = discord.Embed(
                description = f"{member} имеет `{collection.find_one({'_id': member.id})['mes']}` сообщений. `{3000 - mmes}` нужно для получения <@&904714499804790786>",
                color = 0x00ff00
            )
            embed.set_author(name=member, icon_url=member.avatar_url)
            await ctx.send(embed = embed)
        elif mmes < 4999:
            embed = discord.Embed(
                description = f"{member} имеет `{collection.find_one({'_id': member.id})['mes']}` сообщений. `{5000 - mmes}` нужно для получения <@&904715362715721769>",
                color = 0x00ff00
            )
            embed.set_author(name=member, icon_url=member.avatar_url)
            await ctx.send(embed = embed)
        elif mmes > 4999:
            embed = discord.Embed(
                description = f"{member} имеет `{collection.find_one({'_id': member.id})['mes']}` сообщений.",
                color = 0x00ff00
            )
            embed.set_author(name=member, icon_url=member.avatar_url)
            await ctx.send(embed = embed)


@bot.command(aliases = ["bal"])
async def balance(ctx, member: discord.Member = None):
    if member is None:
        total = collection.find_one({'_id': ctx.author.id})['money'] + collection.find_one({'_id': ctx.author.id})['bank']
        embed = discord.Embed(
            description = f"Баланс:\n<:cash:903999146569138216>{collection.find_one({'_id': ctx.author.id})['money']}\nБанк:\n<:cash:903999146569138216>{collection.find_one({'_id': ctx.author.id})['bank']}\nОбщий баланс:\n<:cash:903999146569138216>{total}",
            color = 0x00ff00
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed = embed)
    else:
        total = collection.find_one({'_id': member.id})['money'] + collection.find_one({'_id': member.id})['bank']
        embed = discord.Embed(
            description = f"Баланс:\n<:cash:903999146569138216>{collection.find_one({'_id': member.id})['money']}\nБанк:\n<:cash:903999146569138216>{collection.find_one({'_id': member.id})['bank']}\nОбщий баланс:\n<:cash:903999146569138216>{total}",
            color = 0x00ff00
        )
        embed.set_author(name=member, icon_url=member.avatar_url)
        await ctx.send(embed = embed)


@bot.command(aliases = ["add-messages"])
@commands.has_any_role(902849136041295883, 506864696562024448, 902841113734447214, 933769903910060153)
async def add_messages(ctx, amount: int, member: discord.Member = None):
    if amount > 0:
        if member is None:
            umes = collection.find_one({"_id": ctx.author.id})["mes"]
            collection.update_one({"_id": ctx.author.id}, {"$set": {"mes": umes + amount}})
            embed = discord.Embed(
                description = f"<:check:930367892455850014>Добавлено **{amount}** сообщений {ctx.author.mention}.",
                color = 0x00ff00
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        else:
            mmes = collection.find_one({"_id": member.id})["mes"]
            collection.update_one({"_id": member.id}, {"$set": {"mes": mmes + amount}})
            embed = discord.Embed(
                description = f"<:check:930367892455850014>Добавлено **{amount}** сообщений {member.mention}",
                color = 0x00ff00
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)


@bot.command(aliases = ["remove-messages"])
@commands.has_any_role(902849136041295883, 506864696562024448, 902841113734447214, 933769903910060153)
async def remove_messages(ctx, amount: int, member: discord.Member = None):
    if amount > 0:
        if member is None:
            umes = collection.find_one({"_id": ctx.author.id})["mes"]
            collection.update_one({"_id": ctx.author.id}, {"$set": {"mes": umes - amount}})
            embed = discord.Embed(
                description = f"<:check:930367892455850014>Забрано **{amount}** сообщений у {ctx.author.mention}.",
                color = 0x00ff00
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        else:
            mmes = collection.find_one({"_id": member.id})["mes"]
            collection.update_one({"_id": member.id}, {"$set": {"mes": mmes - amount}})
            embed = discord.Embed(
                description = f"<:check:930367892455850014>Забрано **{amount}** сообщений у {member.mention}.",
                color = 0x00ff00
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)


@bot.command(aliases = ["add-money"])
@commands.has_any_role(902849136041295883, 506864696562024448, 902841113734447214, 933769903910060153)
async def add_money(ctx, amount: int, member: discord.Member = None):
    if amount > 0:
        if member is None:
            umoney = collection.find_one({"_id": ctx.author.id})["money"]
            collection.update_one({"_id": ctx.author.id}, {"$set": {"money": umoney + amount}})
            embed = discord.Embed(
                description = f"<:check:930367892455850014>Добавлено<:cash:903999146569138216>**{amount}** на баланс {ctx.author.mention}.",
                color = 0x00ff00
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        else:
            mmoney = collection.find_one({"_id": member.id})["money"]
            collection.update_one({"_id": member.id}, {"$set": {"money": mmoney + amount}})
            embed = discord.Embed(
                description = f"<:check:930367892455850014>Добавлено<:cash:903999146569138216>**{amount}** на баланс {member.mention}.",
                color = 0x00ff00
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)


@bot.command(aliases = ["remove-money"])
@commands.has_any_role(902849136041295883, 506864696562024448, 902841113734447214, 933769903910060153)
async def remove_money(ctx, amount: int, member: discord.Member = None):
    if amount > 0:
        if member is None:
            umoney = collection.find_one({"_id": ctx.author.id})["money"]
            collection.update_one({"_id": ctx.author.id}, {"$set": {"money": umoney - amount}})
            embed = discord.Embed(
                description = f"<:check:930367892455850014>Забрано<:cash:903999146569138216>**{amount}** с баланса {ctx.author.mention}.",
                color = 0x00ff00
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        else:
            mmoney = collection.find_one({"_id": member.id})["money"]
            collection.update_one({"_id": member.id}, {"$set": {"money": mmoney - amount}})
            embed = discord.Embed(
                description = f"<:check:930367892455850014>Забрано<:cash:903999146569138216>**{amount}** с баланса {member.mention}.",
                color = 0x00ff00
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)


@bot.command()
async def roulette(ctx, color, amount: int):
    num = {
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
    data = collection.find_one({"_id": ctx.author.id})
    minbet, maxbet = 2000, 20000
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
                    if color == num[random.randint(0,36)]:
                        collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": amount}})
                        embed = discord.Embed(
                            description = f"Вы поставили на {color} и выйграли.",
                            color = 0x00ff00
                        )
                        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                        return await ctx.send(embed = embed)
                    else:
                        collection.update_one({"_id": ctx.author.id}, {"$inc": {"money": -amount}})
                        embed = discord.Embed(
                            description = f"Вы поставили на {color} и проиграли.",
                            color = 0xff2400
                        )
                        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                        return await ctx.send(embed = embed)

       
#basic command
@bot.command()
@commands.has_any_role(902849136041295883, 506864696562024448, 902841113734447214, 903384312303472660, 903646061804023808, 903384319937085461, 933769903910060153)
async def warn(ctx, member: discord.Member, *, reason = "Нету"):
    collserver.update_one(
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
    collection.update_one(
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
                    "case": collserver.find_one({"_id": ctx.guild.id})["case"]
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


@bot.command(aliases = ["warnings"])
async def infractions(ctx, member: discord.Member = None):
    if member is None:
        if collection.find_one({"_id": ctx.author.id})["warns"] == 0:
            embed = discord.Embed(
                title = f"Предупреждения участника {ctx.author.name}:",
                description = "Предупреждения отсутствуют.",
                color = 0x42aaff
            )
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(title = f"Предупреждения участника {ctx.author.name}:", color = 0x42aaff)
            user = collection.find_one({"_id": ctx.author.id})
            for value in user["reasons"]:
                embed.add_field(name = f"`Случай #{value['case']}` <t:{value['time']}:f> {bot.get_user(value['author_id'])}", value = f"**Причина:** {value['reason']}", inline = False)

            await ctx.send(embed = embed)
    else:
        if collection.find_one({"_id": member.id})["warns"] == 0:
            embed = discord.Embed(
                title = f"Предупреждения участника {member.name}:",
                description = "Предупреждения отсутствуют.",
                color = 0x42aaff
            )
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(title = f"Предупреждения участника {member.name}:", color = 0x42aaff)
            user = collection.find_one({"_id": member.id})
            for value in user["reasons"]:
                embed.add_field(name = f"`Случай #{value['case']}` <t:{value['time']}:f> {bot.get_user(value['author_id'])}", value = f"**Причина:** {value['reason']}", inline = False)

            await ctx.send(embed = embed)


@bot.command(aliases = ["remove-warn"])
@commands.has_any_role(902849136041295883, 506864696562024448, 902841113734447214, 903384312303472660, 903646061804023808, 903384319937085461, 933769903910060153)
async def remove_warn(ctx, case: int):
    if collection.count_documents({"reasons.case": case}) == 0:
        await ctx.send("Даного случая не найдено.")
    else:
        collection.update_one(
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


@bot.command()
@commands.has_any_role(902849136041295883, 506864696562024448, 902841113734447214, 903384312303472660, 903646061804023808, 933769903910060153)
async def note(ctx, member: discord.Member, *, reason_note = "Нету"):
    collserver.update_one(
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
    collection.update_one(
        {
            "_id": member.id
        },
        {
            "$push": {
                "notes": {
                    "author_id": ctx.author.id,
                    "reason_note": reason_note,
                    "time": timenote,
                    "note": collserver.find_one({"_id": ctx.guild.id})["note"]
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


@bot.command()
async def notes(ctx, member: discord.Member = None):
    if member is None:
        if collection.find_one({"_id": ctx.author.id})["note"] == 0:
            embed = discord.Embed(
                title = f"Заметки участника {ctx.author.name}:",
                description = "Заметки отсутствуют.",
                color = 0x42aaff
            )
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(title = f"Заметки участника {ctx.author.name}:", color = 0x42aaff)
            user = collection.find_one({"_id": ctx.author.id})
            for value in user["notes"]:
                embed.add_field(name = f"`Заметка #{value['note']}` <t:{value['time']}:f> {bot.get_user(value['author_id'])}", value = f"**Заметка:** {value['reason_note']}", inline = False)

            await ctx.send(embed = embed)
    else:
        if collection.find_one({"_id": member.id})["note"] == 0:
            embed = discord.Embed(
                title = f"Заметки участника {member.name}:",
                description = "Заметки отсутствуют.",
                color = 0x42aaff
            )
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(title = f"Заметки участника {member.name}:", color = 0x42aaff)
            user = collection.find_one({"_id": member.id})
            for value in user["notes"]:
                embed.add_field(name = f"`Заметка #{value['note']}` <t:{value['time']}:f> {bot.get_user(value['author_id'])}", value = f"**Заметка:** {value['reason_note']}", inline = False)

            await ctx.send(embed = embed)


@bot.command(aliases = ["remove-note"])
@commands.has_any_role(902849136041295883, 506864696562024448, 902841113734447214, 903384312303472660, 903646061804023808, 933769903910060153)
async def remove_note(ctx, note: int):
    if collection.count_documents({"notes.note": note}) == 0:
        await ctx.send("Даного случая не найдено.")
    else:
        collection.update_one(
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


@bot.command(aliases = ["purge"])
@commands.has_any_role(902849136041295883, 506864696562024448, 902841113734447214, 903384312303472660, 903646061804023808, 903384319937085461, 933769903910060153)
async def clear(ctx, amount: int):
    if amount > 0:
        if amount < 200:
            number = amount + 1
            await ctx.channel.purge(limit=number)
            await ctx.send(f"<:check:930367892455850014>Удалено {amount} сообщений.")


@bot.command()
async def mute(ctx, member: discord.Member, time):
    time_convert = {"s":1, "m":60, "h":3600, "d":86400, "w":604800}
    tempmute = int(time[0]) * time_convert[time[-1]]
    await asyncio.sleep(tempmute)
    await ctx.send(f"{tempmute}")


@bot.command()
async def test(ctx):
    time = int(datetime.datetime.utcnow().timestamp())
    await ctx.send(embed = discord.Embed(
        description = f"test {time}",
        timestamp = datetime.datetime.utcnow(),
    ),
        components = [
            Button(style = ButtonStyle.green, label = "Accept"),
            Button(style = ButtonStyle.red, label = "Decline"),
            Button(style = ButtonStyle.URL, label = "YouTube" , url = "https://www.youtube.com/")
        ]
    )

    response = await bot.wait_for("button_click")
    if response.channel == ctx.channel:
        if response.component.label == "Accept":
            await response.respond(content = "Вы согласились")
        else:
            await ctx.respond(content = "Вы отказались")


@bot.command()
async def help(ctx):
    embed1 = discord.Embed(title="Страница 1", description='test 1')
    embed2 = discord.Embed(title="Страница 2", description='test 2')
    embed3 = discord.Embed(title="Страница 3", description='test 3')
    embeds = [embed1, embed2, embed3]
    message = await ctx.send(embed=embed1)
    page = Paginator(bot, message, only=ctx.author, use_more=False, footer=False, embeds=embeds)
    await page.start()


@bot.command()
async def ping(ctx):
    embed = discord.Embed(
        description = f"Ping: {round(bot.latency * 1000)}ms",
        color = 0x00ff00
    )
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    await ctx.send(embed = embed)


@bot.command()
async def rand(ctx, amount = 1, *, args):
    spisok = args.split()
    rand = random.choices(spisok, k=amount)
    await ctx.send(", ".join(rand))


#owner command
@bot.command()
@commands.is_owner()
async def removevar(ctx):
    collection.delete_many({})
    await ctx.send('Переменые удалены')

bot.run('ODQwMTUzNzEwMzY1Mzc2NTgz.YJUEHQ.tZUIYVzFtcoDBjdfweFmc_h7uiw')
