import random
from random import randint
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot
import praw


blameh = praw.Reddit(client_id='ofpU7MVEBEPBTg',
                  client_secret='f44rSSXENKk1znRfZhsQZrEzn64',
                  username = 'murtreddit',
                  password = '1843184318431843',
                  user_agent = 'PRAWlearn.1' )



BOT_PREFIX = ("?", "!")
client = Bot(command_prefix = BOT_PREFIX)
TOKEN = "NDgyNjA0ODk2NTcxNjIxMzk2.DmHYoQ.hs719DNu2YZaVxXC6ZrwLmDwd64"

@client.event

async def on_ready():
	print ("Logged in as " + client.user.name)


@client.event
async def lel(message):
    if message.author == client.user:
        return
    if message.content.startswith('!','?'):
        return 1
    if message.content.startswith('hello'):
        author = message.author
        channel = message.channel
        await message.channel.send(f"Hello, {author} nice to see you")
        return


@client.command(name = 'darkjoke',
                description = 'gives the top ten darkjokes',
                brief = 'some dark humour for the edgy people out there',
                aliases = ['dark', 'darkhumour'],
                pass_context = 'True')
async def blargh(message):
        list = []
        for submission in blameh.subreddit('darkjokes').new(limit=20):
            chanl = message.channel
            list.append(submission.title + submission.selftext)
        print(list)
        v = list[randint(0,19)]
        print (v)
        await chanl.send(v)

@client.command(name= 'cozyplaces',
                description = 'teleports you to the coziest places on earth',
                brief = 'teleports you to the coziest places on earth',
                aliases = ['cozyplace'],
                pass_context = 'True')
async def sfhuw(message):
    list = []
    for submission in blameh.subreddit('cozyplaces').new(limit=20):
        channl = message.channel
        list.append(submission.url)
    print(list)
    v = list[randint(0,19)]
    print (v)
    await channl.send(v)

@client.command(name= 'earthpics',
                description = 'sends the best earth pics',
                brief = 'sends the best earth pics',
                aliases = ['earthpic'],
                pass_context = 'True')
async def sfhu(message):
    list = []
    for submission in blameh.subreddit('earthporn').new(limit=20):
        chanl = message.channel
        list.append(submission.url)
    print(list)
    v = list[randint(0,19)]
    print (v)
    await chanl.send(v)


















@client.command(name = 'redditpull',
                description = 'pulls a random pic/gif from a subreddit of your choice',
                brief = 'pulls a random pic/gif from a subreddit of your choice',
                aliases = ['reddit', 'redditgif'],
                pass_context = 'True')
async def blehhh(ctx):
    def lelel(message):
        hahah = content.message
    list = []
    for submission in blameh.subreddit('str(hahah)').new(limit=20):
        chanl = message.channel
        list.append(submission.url)
    print(list)
    v = list[randint(0,19)]
    print (v)
    await chanl.send(v)




client.run(TOKEN)
