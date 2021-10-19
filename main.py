import discord
import os
import random
from keep_alive import keep_alive

client = discord.Client()

commonWords = ['next', 'release', 'new', 'come', 'out']

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="your every step"))

@client.event
async def on_message(message):

  if message.author == client.user:
    return
  
  i = 0
  msgCont = message.content.lower()

  if ('when' in msgCont) and ('chapter' in msgCont) or ('chap' in msgCont):
    
    msgSplit = msgCont.split()

    print(msgSplit)

    if len(msgSplit) > 2:  
      for word in commonWords:
        if word in msgSplit:
          if "does" in msgSplit:
            i = i + 1
          if "gonna" in msgSplit:
            i = i + 1

      print(i)
      if i > 0:
        print("OK")
        opt = random.randint(1, 2)
        if opt == 1:
          await message.channel.send("When its done being translated :p")
        if opt == 2:
          await message.channel.send('When its ready to be released :p')

    else:
      print("OK")
      opt = random.randint(1, 2)
      if opt == 1:
        await message.channel.send("When its done being translated :p")
      if opt == 2:
        await message.channel.send('When its ready to be released :p')

    #await message.channel.send('Bot in testing mode, message has been recognized')  
  
  if ('gib' in msgCont) and ('chapter' in msgCont):
    await message.channel.send("nay, thee wilt asketh nicely 'r as the ov'rl'rds has't did state +10 minutes to releaseth")
  
  if ('at' in msgCont) and ('which' in msgCont) and ('hour' in msgCont) and ("chapt'r" in msgCont):
    await message.channel.send("aft'r t done being did translate :p") 

keep_alive()
client.run(os.environ['token'])
