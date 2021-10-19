import discord
import os
import random
from keep_alive import keep_alive

client = discord.Client()

commonWords = ['next', 'release', 'new', 'come', 'out']
sentenceKeyWord = ['does', 'gonna', 'going']

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

  if ('when' in msgCont) and ('chapter' in msgCont):
    
    msgSplit = msgCont.split()

    print(msgSplit)

    if len(msgSplit) > 2:  
      for word in commonWords:
        if word in msgSplit:
          for sk in sentenceKeyWord:
            if sk in msgSplit:
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
  
  #I got tried of trying to make it work :p
  if message.content.startswith('when is chapter'):
    opt = random.randint(1, 2)
    if opt == 1:
      await message.channel.send("When its done being translated :p")
    if opt == 2:
      await message.channel.send('When its ready to be released :p')
  
  if message.content.startswith('where new chap'):
    await message.channel.send("*Demonic voice* In the depths of my stomatch often reffered to as H E L L")
    await message.channel.send("*normal voice* Want me to send you there (:")
  
  if message.content.startswith('where chap'):
    await message.channel.send("*Demonic voice* In the depths of my stomatch often reffered to as H E L L")
    await message.channel.send("*normal voice* Want me to send you there (:")
  
  if message.content.startswith('when chap'):
      await message.channel.send("When its done being translated :p")
  
  if message.content.startswith('when new chap'):
    opt = random.randint(1, 2)
    if opt == 1:
      await message.channel.send("When its done being translated :p")
    if opt == 2:
      await message.channel.send('When its ready to be released :p')
  
  if message.content.startswith('when will new chapter'):
    opt = random.randint(1, 2)
    if opt == 1:
      await message.channel.send("When its done being translated :p")
    if opt == 2:
      await message.channel.send('When its ready to be released :p')
  
  if message.content.startswith('when will chapter'):
    opt = random.randint(1, 2)
    if opt == 1:
      await message.channel.send("When its done being translated :p")
    if opt == 2:
      await message.channel.send('When its ready to be released :p')


  if ('gib' in msgCont) and ('chapter' in msgCont):
    await message.channel.send("nay, thee wilt asketh nicely 'r as the ov'rl'rds has't did state +10 minutes to releaseth")
  
  if ('at' in msgCont) and ('which' in msgCont) and ('hour' in msgCont) and ("chapt'r" in msgCont):
    await message.channel.send("aft'r t done being did translate :p") 

  #so it can work with chap
  if ('when' in msgCont) and ('chap' in msgCont):
    
    msgSplit = msgCont.split()

    print(msgSplit)

    if len(msgSplit) > 2:  
      for word in commonWords:
        if word in msgSplit:
          for sk in sentenceKeyWord:
            if sk in msgSplit:
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
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  if message.content.startswith("!**!#!meme"):
    await message.channel.send("Put the memes in the bag onii-chan *points gun*")


keep_alive()
client.run(os.environ['token'])
