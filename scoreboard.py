import discord      #IMPORTED FOR THE DISCORD API
from discord.ext import commands #IMPORTED FOR DISCORD BOT COMMANDS
import json
import random
client = commands.Bot(command_prefix = '~') #COMMANDS WILL BE "BOT <COMMAND>"
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('~help: for help'))
    print("Bot is ready")
with open("users.json") as fp:
        users = json.load(fp)
def save_users():
    with open("users.json", "w+") as fp:
        json.dump(users, fp, sort_keys=True, indent=4)
def add_points(user: discord.User, points: int):
    id = user.id
    id = str(id)
    if id not in users:
        users[id] = {}
        users[id]["points"] = users[id].get("points", int(0)) + int(points)
        print("{} now has {} points".format(user.name, users[id]["points"]))
        save_users()
    else:
        users[id]["points"] = users[id].get("points", int(0)) + int(points)
        print("{} now has {} points".format(user.name, users[id]["points"]))
        save_users()
        messageAuthorLast = messageAuthor
def get_points(user: discord.User):
    id = user.id
    id = str(id)
    if id in users:
        return users[id].get("points", 0)
        return 0
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print("{} sent a message".format(message.author.name))
    if message.content.lower().startswith("~points"):
        sender = message.author.id
        sender = str(sender)
        #print(sender +"IS THE ID")
        author = message.author
        pfp = author.avatar_url
        pts = users[sender].get("points", 0)
        pts = str(pts)
        colorChoice = random.randint(1,5)
        if colorChoice == 1:
            embed=discord.Embed(title="Scoreboard!", description=str(message.author) +' has ' +pts  +' points!'.format(message.author), color=0x37109f)
            embed.set_image(url=(pfp))
            await message.channel.send(embed=embed)
        elif colorChoice == 2:
            embed=discord.Embed(title="Scoreboard!", description=str(message.author) +' has ' +pts  +' points!'.format(message.author), color=0xf41f9f)
            embed.set_image(url=(pfp))
            await message.channel.send(embed=embed)
        elif colorChoice == 3:
            embed=discord.Embed(title="Scoreboard!", description=str(message.author) +' has ' +pts  +' points!'.format(message.author), color=0xff709f)
            embed.set_image(url=(pfp))
            await message.channel.send(embed=embed)
        elif colorChoice == 4:
            embed=discord.Embed(title="Scoreboard!", description=str(message.author) +' has ' +pts  +' points!'.format(message.author), color=0x18f36c)
            embed.set_image(url=(pfp))
            await message.channel.send(embed=embed)
        elif colorChoice == 5:
            embed=discord.Embed(title="Scoreboard!", description=str(message.author) +' has ' +pts  +' points!'.format(message.author), color=0xffffff)
            embed.set_image(url=(pfp))
            await message.channel.send(embed=embed)
        #msg = "`You have {} points!`".format(get_points(message.author))
        #await message.channel.send(msg)
    elif message.content.lower().startswith("~mpoints"):
        #print(message.mentions[0].id)
        usrPts = message.mentions[0].id
        usrPts = str(usrPts)
        #print(users[usrPts].get("points", 0))
        #if message.mentions[0].id not in users:
        #    print("They have no points")
        #    msg1 = "```They have no points!```"
        #else:
        author = message.mentions[0]
        pfp = author.avatar_url 
 #       #print(users[usrPts].get("points", 0))
        pts = users[usrPts].get("points", 0)
        colorChoice = random.randint(1,5)
        embed=discord.Embed(title="Scoreboard!", description=str(author) +' has ' +str(pts)  +' points!')#.format(color=0xff109f)
        embed.set_image(url=(pfp))
        await message.channel.send(embed=embed)
        #msg1 = "```They have {} points!```".format(users[usrPts].get("points", 0))
        #await message.channel.send(msg1)
    elif message.content.lower().startswith("~help"):
        await message.channel.send("```V2.0 Scoreboard written by LinuxDaily\n\n~points:  Shows how many points you have\n~mpoints: Shows how many points any mentioned member has\n~help: Shows this page\n\nReport any bugs or suggestions to LinuxDaily```")
    else:
        add_points(message.author, 1)
        save_users()
#RUN AS SCOREBOARD (FOR STABLE RELEASE)
client.run('Super Secret Token')
