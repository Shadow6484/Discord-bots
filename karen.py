#Karen bot
import discord      #IMPORTED FOR THE DISCORD API
from discord.ext import commands #IMPORTED FOR DISCORD BOT COMMANDS
import time         #IMPORTED FOR THE WAITTIME VARIABLE TO PROVIDE A PAUSE INBETWEEN MESSAGES
import random       #IMPORTED FOR THE RANDOM SENTENCE GENERATOR AND THE RANDOM WAIT TIMES TO MAKE MESSAGES more HUMAN LIKE
client = commands.Bot(command_prefix = 'karen') 
#events
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Calling your manager'))
    print('Bot is running')
#    await message.channel.send("Karen is back!")
@client.event
async def on_message(message):
    #DEBUG LINES
    serverSent = message.guild
    serverSent = str(serverSent)
    #print(type(serverSent))
    #print(serverSent)
    if " ass" in message.content or " shit" in message.content or " bitch" in message.content or " fuck" in message.content or " Fuck" in message.content or " Shit" in message.content or " Ass" in message.content or " Bitch" in message.content:
        choice = random.randint(1,2)
        await message.channel.send("Watch your profanity")
        await message.channel.send("Admin this guy is swearing, its offensive!!")
        if choice == 1:
            await message.channel.send("I am triggered!")
    elif " hello " in message.content or " Hello " in message.content or " hi " in message.content or " Hi " in message.content or " Greetings " in message.content or " greetings " in message.content:
        choice = random.randint(1,3)
        if choice == 1:
            await message.channel.send('How are you doing?')
        elif choice == 2:
            await message.channel.send('Howdy!')
        elif choice == 3:
            await message.channel.send('Hola!')
    elif "karen" in message.content or "Karen" in message.content:
        await message.channel.send("https://tenor.com/bipzW.gif")
    elif "triggered" in message.content or "trigger" in message.content or "Triggered" in message.content or "Trigger" in message.content:
        await message.channel.send("https://tenor.com/YCNG.gif")
    elif "Good" in message.content or "good" in message.content:
        await message.channel.send("Thats nice to hear!")
    elif "how are you" in message.content or "How are you" in message.content or "How Are You" in message.content:
        choice = random.randint(1,3)
        if choice == 1:
            await message.channel.send("I am doing great! thank you so much for asking")
        elif choice == 2:
            await message.channel.send("Ive been better but i'll go on, thanks for asking!")
        elif choice == 3:
            await message.channel.send("Doing great, I hope you're doing great too!")
    elif "reee" in message.content or "Reee" in message.content or "REEE" in message.content:
        await message.channel.send("https://tenor.com/bpOGl.gif")
#connect bot program to discord api
client.run('Super Secret Token')
