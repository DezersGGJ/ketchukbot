#biblites
import contextlib
import discord
import datetime
import random
import json
import requests
import os
import asyncio
import humanize
import io
import textwrap
import schedule
import time
from PIL import Image, ImageFont, ImageDraw
from discord.ext import commands, tasks
from pymongo import MongoClient
from Cybernator import Paginator
from discord_components import DiscordComponents, Button, ButtonStyle, Select, SelectOption
from func import *
from traceback import format_exception
from utils.util import clean_code, Pag


bot = commands.Bot(command_prefix = '#', intents = discord.Intents.all())
bot.remove_command('help')
cluster = MongoClient("mongodb+srv://DezersGG:Weerweer333@cluster0.b9xjp.mongodb.net/ecodb?retryWrites=true&w=majority")
collection = cluster.ecodb.colldb
collserver = cluster.ecodb.collserver
    
@bot.event
async def on_ready():
    print("Bot connected to the server")
    DiscordComponents(bot)
    await bot.change_presence(status = discord.Status.online, activity = discord.Game('#help'))
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
                "endurance": 100,
                "cdrob": 0,
                "weeklymes": 0
            }
            server = {
                "_id": guild.id,
                "case": 0,
                "note": 0,
                "quiz": []
            }
            if collection.count_documents({"_id": member.id}) == 0:
                collection.insert_one(user)
            if collserver.count_documents({"_id": guild.id}) == 0:
                collserver.insert_one(server)

@bot.event
async def on_member_join(member):
    image = Image.open('banners.jpg')
    img = image.resize((960, 540))
    idraw = ImageDraw.Draw(img)
    title = ImageFont.truetype('fint.ttf', size = 80)
    name = str(member.guild.member_count)
    boost = str(member.guild.premium_subscription_count)
    idraw.text((285, 347), name, font = title, fill = '#ffd6da')
    idraw.text((575, 345), boost, font = title, fill = '#ffd6da')
    img.save('image.jpg')
    with open("image.jpg", 'rb') as image:
        await member.guild.edit(banner=image.read())
    mutes = load_json("jsons/mutes.json")
    if str(member.id) in mutes:
        role = discord.utils.get(member.guild.roles, id=902942596962328656)
        await member.add_roles(role)
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
        "endurance": 100,
        "cdrob": 0,
        "weeklymes": 0
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
    image = Image.open('banners.jpg')
    img = image.resize((960, 540))
    idraw = ImageDraw.Draw(img)
    title = ImageFont.truetype('fint.ttf', size = 80)
    name = str(member.guild.member_count)
    boost = str(member.guild.premium_subscription_count)
    idraw.text((285, 347), name, font = title, fill = '#ffd6da')
    idraw.text((575, 345), boost, font = title, fill = '#ffd6da')
    img.save('image.jpg')
    with open("image.jpg", 'rb') as image:
        await member.guild.edit(banner=image.read())
    if member.bot == False:
      embed = discord.Embed(
          description = f"Участник **{member.name}** вышел с сервера.",
          color = 0x42aaff
      )
      icon = str(member.guild.icon_url)
      embed.set_thumbnail(url = icon)
      image = Image.open('banners.jpg')
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
            data = collection.find_one({"_id": message.author.id})
            collection.update_one({"_id": message.author.id}, {"$inc": {"mes": 1}})
            collection.update_one({"_id": message.author.id}, {"$inc": {"weeklymes": 1}})
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

    await bot.process_commands(message)

@bot.command()
async def rand(ctx, amount = 1, *, args):
    spisok = args.split()
    rand = random.choices(spisok, k=amount)
    await ctx.send(", ".join(rand))

@bot.command()
async def answer(ctx, otvet):
    if ctx.channel.id == 938066308011003904:
        user = collserver.find_one({"_id": ctx.guild.id})
        for value in user["quiz"]:
            if otvet.lower() == value['answer']:
                collserver.update_one(
                    {
                        "quiz.answer": otvet.lower()
                    },
                    {
                        "$pull": {
                            "quiz": {
                                "answer": otvet.lower()
                            }
                        }
                    }
                )
                embed = discord.Embed(
                    description = f"{ctx.author.mention} ответил на вопрос.\n**Ответ:** {otvet}.",
                    color = 0x00ff00
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await bot.get_channel(938066272946622506).send(embed=embed)
                
@bot.command()
async def select(ctx):
    await ctx.send('Пункт', components=[
        Select(
            placeholder="Выберите пункт",
            options=[
                SelectOption(
                    emoji='💵',
                    label='Экономика',
                    description='Экономика',
                    value='e1'
                ),
                SelectOption(
                    emoji='📜',
                    label='Модерация',
                    description='Модерация',
                    value='e2'
                )
            ]
        )
    ])
    i = 1
    while i == 1:
        try:
            res = await bot.wait_for("select_option", check=None)
            label = res.component[0]
            if res.channel == ctx.channel:
                if label == "Экономика":
                    await res.respond(content="Экономика")
                else:
                    await res.respond(content="Модерация")
        except discord.NotFound:
            print('error')
    await asyncio.sleep(60)
    i += 1


@bot.command()
@commands.is_owner()
async def eval(ctx, *, code):
    code = clean_code(code)

    local_variables = {
        "discord": discord,
        "commands": commands,
        "bot": bot,
        "ctx": ctx,
        "channel": ctx.channel,
        "author": ctx.author,
        "guild": ctx.guild,
        "message": ctx.message
    }

    stdout = io.StringIO()

    try:
        with contextlib.redirect_stdout(stdout):
            exec(
                f"async def func():\n{textwrap.indent(code, '    ')}", local_variables,
            )

            obj = await local_variables["func"]()
            result = f"{stdout.getvalue()}\n-- {obj}\n"
    except Exception as e:
        result = "".join(format_exception(e, e, e.__traceback__))

    pager = Pag(
        timeout=100,
        entries=[result[i: i + 2000] for i in range(0, len(result), 2000)],
        length=1,
        prefix="```py\n",
        suffix="```"
    )

    await pager.start(ctx)

#owner command
@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    await ctx.message.add_reaction('<:yes:903316080456523787>')
    bot.load_extension(f"cogs.{extension}")


@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    await ctx.message.add_reaction('<:yes:903316080456523787>')
    bot.unload_extension(f"cogs.{extension}")


@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    await ctx.message.add_reaction('<:yes:903316080456523787>')
    bot.unload_extension(f"cogs.{extension}")
    bot.load_extension(f"cogs.{extension}")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run('ODQwMTUzNzEwMzY1Mzc2NTgz.YJUEHQ.MN5iSz4uR9uA1Oo0JhrTttKrKTA')
