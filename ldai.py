#Bot code for LinuxDaily's AI Counterbot
#production started March/11/2020
#version 3.4 (10/15/2020)

#currently has a full vocabulary size of 9082 when using default wordlists
import discord      #IMPORTED FOR THE DISCORD API
from discord.ext import commands #IMPORTED FOR DISCORD BOT COMMANDS
import os           #IMPORTED TO CHECK FILE PATHS BEFORE START
import time         #IMPORTED FOR THE WAITTIME VARIABLE TO PROVIDE A PAUSE INBETWEEN MESSAGES
import random       #IMPORTED FOR THE RANDOM SENTENCE GENERATOR AND THE RANDOM WAIT TIMES TO MAKE MESSAGES more HUMAN LIKE
client = commands.Bot(command_prefix = '~') #COMMANDS WILL BE "BOT <COMMAND>"
#events
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('~assist for help'))
    print('Bot is running')
#Commented out for integration into another bot
#@client.event
#async def on_message(message):
#    if message.author == client.user:
#        return
#    if message.content.startswith('shit') or message.content.startswith('fuck') or message.content.startswith('bitch'):
#        await message.channel.send("Watch your mouth boy")
#@client.event
#async def on_message(message):
#    if message.author == client.user:
#        return
#
#    if message.content.startswith('hello') or message.content.startswith('hi') or message.content.startswith('greetings') or message.content.startswith('Hi') or message.content.startswith('Hello'):
#        choice = random.randint(1,6)
#        if choice == 1:
#            await message.channel.send('Hello!')    
#        if choice == 2:
#            await message.channel.send('Hi')
#        if choice == 3:
#            await message.channel.send('How are you doing?')
#        if choice == 4:
#            await message.channel.send('Greetings!')
#        if choice == 5:
#            await message.channel.send('Howdy!')
#        if choice == 6:
#
#            await message.channel.send('Hola!') 
#        else:
#            return
#------------------------------------------------------
#commands
@client.command()
async def linux(ctx):
    await ctx.send("https://youtube.com/c/linuxdaily")
@client.command()
async def testingcommand(ctx):
    await ctx.send("this is line 1 \n this is line2")
@client.command()
async def msbad(ctx):
    await ctx.send("Yes")
@client.command()
async def rules(ctx):
        await ctx.send("```Rules and Regulations\n1. Be respectful\n2. Don't be annoying\n3. No unecessary pinging\n4. No spamminnRules are subject to change at any time\n\nAll politics and arguments shall be done in the war-zone channel.\n\n\n\nRules will be enforced in this order:\n1: Warning by an admin\n2: Mute determined by an admin\n3: Kicked from server\n4: Banned from server```")
@client.command()
async def hi(ctx):
        choice = random.randint(1,6)
        if choice == 1:
            await ctx.send("Hello!")
        if choice == 2:
            await ctx.send("Hi!")
        if choice == 3:
            await ctx.send("Howdy!")
        if choice == 4:
            await ctx.send("Hello! :)")
        if choice == 5:
            await ctx.send("Hola!")
        if choice == 6:
            await ctx.send("Greetings")
@client.command()
async def speak(ctx):
        pathExists = os.path.exists('/etc/lists/')
        if pathExists == False:
            print("There is no /etc/lists folder, verify that the bot is installed correctly")
            sys.exit()
        try:
            pnoun=[]
            nouns=[]
            verbs=[]
            adj=[]
            # LOAD ALL VOCABULARY INTO MEMORY
            try:
                try:
                    with open("/etc/lists/pnoun.txt") as proNouns:
                        for line in proNouns:
                            line.rstrip()
                            pnoun.append(line)
                except:
                    print("Error loading pnoun.txt")
                try:
                    with open("/etc/lists/nouns.txt") as noun:
                        for line in noun:
                            line.rstrip()
                            nouns.append(line)
                except:
                    print("Error loading nouns.txt")
                try:
                    with open("/etc/lists/verbs.txt") as verb:
                        for line in verb:
                            line.rstrip()
                            verbs.append(line)
                except:
                    print("Error loading verbs.txt")
                try:
                    with open("/etc/lists/adj.txt") as adjective:
                        for line in adjective:
                            line.strip()
                            adj.append(line)
                except:
                    print("Error loading adj.txt")
            except:
                print("There was an error loading the full vocabulary")
                print("")
                print("Make sure you have in your current directory:")
                print("pnoun.txt          filled with pronouns")
                print("nouns.txt          filled witn nouns")
                print("verbs.txt          filled with verbs")   
                print("adj.txt            filed with adjectives")
                print("Put all of these files in '/etc/lists/` as this is where the program looks")
                print("")
    #UNCOMMENT IF THERE ARE LIST ERRORS TO DEBUG
    #print(pnoun)
    #print(nouns)
    #print(verbs)
    #print(adj)
            choice = random.randint(1,5)
            if choice == 1:
                messageOutput = random.choice(pnoun).strip('\n') +' '  +random.choice(nouns).strip('\n') +' ' +random.choice(verbs).strip('\n') +' ' +random.choice(adj).strip('\n')
            elif choice == 2:
                messageOutput = random.choice(nouns).strip('\n') +' ' + random.choice(verbs).strip('\n') +' ' +random.choice(adj).strip('\n')
            elif choice == 3:
                messageOutput = random.choice(nouns).strip('\n') + ' and ' + random.choice(nouns).strip('\n') + ' ' +random.choice(verbs).strip('\n')
            elif choice == 4:
                messageOutput = random.choice(pnoun).strip('\n') + ' ' +random.choice(verbs).strip('\n') + ' '+ random.choice(nouns).strip('\n')
            elif choice == 5:
                messageOutput = random.choice(nouns).strip('\n') + ' ' +random.choice(verbs).strip('\n')
            elif choice == 6:
                messageOutput = random.choicE(nouns).strip('\n') + ' ' +random.choice(adj).strip('\n')
            await ctx.send(messageOutput)
        except:
            print("Bot has stopped.")
@client.command()
async def invite(ctx):
        await ctx.send("Here is an invite link: https://discord.gg/a445N5KUtQ")

@client.command()
@commands.has_role("Admin")
async def erase(ctx, amount=1):
        vidToDisp = random.randint(1,4)
        if vidToDisp == 1:
            await ctx.send("https://tenor.com/bdgIM.gif")
        if vidToDisp == 2:
            await ctx.send("https://tenor.com/JSfl.gif")
        if vidToDisp == 3:
            await ctx.send("https://tenor.com/1j5w.gif")
        if vidToDisp == 4:
            await ctx.send("https://tenor.com/Qgek.gif")
        time.sleep(3)
        await ctx.channel.purge(limit=amount+2)
@client.command()
async def eightball(ctx):
        choice = random.randint(1,10)
        if choice == 1:
            await ctx.send("It is certain!")
        elif choice == 2:
            await ctx.send("Reply hazy try again")
        elif choice == 3:
            await ctx.send("My sources say no")
        elif choice == 4:
            await ctx.send("Outlook good")
        elif choice == 5:
            await ctx.send("Very doubtful")
        elif choice == 6:
            await ctx.send("Cannot predict now")
        elif choice == 7:
            await ctx.send("Signs point to yes")
        elif choice == 8:
            await ctx.send("Concentrate and ask again")
        elif choice ==9:
            await ctx.send("You may rely on it.")
        elif choice == 10:
            await ctx.send("Ask again later.")
@client.command()
async def assist(ctx):
        await ctx.send("```This is the help page, type bot before your command to call the command\nassist     Display this message\nspeak      Generates a random sentence for you\nhi         Just says hi back\nrules      Display the rules and regulations\nmsbad      Tells you if Microsoft is bad\nlinux      Displays LinuxDaily's Youtube channel\ninvite     Displays a non-expiring invite to this server\nmball      Simple magic 8 ball```")
@client.command()
@commands.has_permissions(administrator=True)
async def adminassist(ctx):
        await ctx.send("Admins only :)")
        await ctx.send("~warn      Gives a player a warning")
        await ctx.send("~kick      Kicks a member out")
        await ctx.send("~ban       Bans a member")
        await ctx.send("~erase     Clears the chat")

@client.command()
@commands.has_role("Admin")
async def kick(ctx, member : discord.Member, *, reason=None):
        await ctx.send("https://tenor.com/8bnA.gif")
        time.sleep(5)
        await member.kick(reason=reason)
        time.sleep(5)
        await ctx.channel.purge(limit=2)
@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
        await ctx.send("you got 5 seconds to say your last words")
        time.sleep(5)
        await ctx.send("https://tenor.com/8bnA.gif")
        time.sleep(5)
        await member.ban(reason=reason)
        time.sleep(5)
        await ctx.channel.purge(limit=3)
#connect bot program to discord api
client.run('super secret token')
