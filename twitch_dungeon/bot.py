import os
import sys
from twitchio.ext import commands
from sqlalchemy.ext.declarative import declarative_base

import twitch_dungeon.settings as settings
import twitch_dungeon.db.tables as tables

config = settings
Base = declarative_base()

bot = commands.Bot(
    # set up the bot
    irc_token=os.environ["TMI_TOKEN"],
    client_id=os.environ["CLIENT_ID"],
    nick=os.environ.get("BOT_NICK", "Alaveus"),
    prefix=os.environ.get("BOT_PREFIX", "!"),
    initial_channels=[os.environ["CHANNEL"]],
)


@bot.event
async def event_ready():
    """Called once when the bot goes online."""
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ["CHANNEL"], "/me has arrived!")


@bot.command(name="alaveus")
async def overview(ctx):
    """Describe the rules of the dungeon"""
    rules = """
        I am Alaveus. For the meager price of 10 chalupas,
        I can transport you deep into the heart of a mythic  dungeon
        where treasure and glory await those who dare enter!
    """
    await ctx.send(rules)


@bot.command(name="rollchar")
async def rollchar(ctx):
    db = tables.database
    await db.connect()
    query = tables.characters.select().where(
        tables.characters.c.name == ctx.author.name
    )
    response = await db.execute(query=query)
    for row in response:
        print(row)
    if response.len != 0:
        ctx.send(response.next())
        return

    query = tables.characters.insert()
    values = {
        "name": ctx.author.name,
        "level": 1,
        "STR": 0,
        "DEX": 0,
        "CON": 0,
        "WIS": 0,
        "INT": 0,
    }
    await db.execute(query=query, values=values)
    await ctx.send(ctx.author.name)


def run():
    print(sys.path)
    bot.run()