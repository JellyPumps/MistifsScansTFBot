import discord
import os
import random
from keep_alive import keep_alive

client = discord.Client()

commonWords = ['next', 'release', 'new', 'come', 'out']
sentenceKeyWord = ['does', 'gonna', 'going']
commands = ['^meme', '^hi', '^r34', '^bye!']

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
  
  if message.content.startswith('where is chap'):
    await message.channel.send("*Demonic voice* In the depths of my stomatch often reffered to as H E L L")
    await message.channel.send("*normal voice* Want me to send you there (:")
  
  if message.content.startswith('where is new chap'):
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
  
  if message.content.startswith('when is the new chap'):
    opt = random.randint(1, 2)
    if opt == 1:
      await message.channel.send("When its done being translated :p")
    if opt == 2:
      await message.channel.send('When its ready to be released :p')
  
  if message.content.startswith('new chapter when'):
    opt = random.randint(1, 2)
    if opt == 1:
      await message.channel.send("When its done being translated :p")
    if opt == 2:
      await message.channel.send('When its ready to be released :p')
  
  if message.content.startswith('new chap when'):
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
  if message.content.startswith("^help"):
    await message.channel.send("Here are the commands I answer: {0}".format(commands))
  #
  #
  #
  # 
  if message.content.startswith("^meme"):
    memeopt = random.randint(1, 4)
    print(memeopt)
    if memeopt == 1:
      await message.channel.send("Put the memes in the bag onii-chan *points gun*")
    if memeopt == 2:
      await message.channel.send("Time to sexually harass Iruma-chi")
    if memeopt == 3:
      await message.channel.send("Me:Makes  Pikachu meme in text form\nReddit: 7 upvotes\nMe:\n⣿⣿⣿⣿⣿⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿\n⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿\n⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠿⠻⠿⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿\n⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠀⠸⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠤⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⢿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠀⠠⣿⣿⣷⠀⢸⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⡀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿\n⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣠⣤⣶⣶\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢰⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⣀⣾⣿⣿⣿⣿")
    if memeopt == 4:
      await message.channel.send("Did you know? In chapter 109, Clara slept with Iruma.")
  #
  #
  #
  #
  if message.content.startswith("^hi"):
    await message.channel.send("Hello o/ *Waves*")
  #
  #
  #
  #
  if message.content.startswith("^bye"):
    await message.channel.send("Bye! *Waves*")
  #
  #
  #
  #
  if message.content.startswith("^GoodbyeForever"):
    await message.channel.send("F-fine I didn't care for you anyway *snif*")
  #
  #
  #
  #
  if message.content.startswith("^r34"):
    hornopt = random.randint(1, 12)
    if hornopt == 1:
      await message.channel.send(file=discord.File('1.jpg'))
    if hornopt == 2:
      await message.channel.send(file=discord.File('2.jpg'))
    if hornopt == 3:
      await message.channel.send(file=discord.File('3.jpg'))
    if hornopt == 4:
      await message.channel.send(file=discord.File('4.jpg'))
    if hornopt == 5:
      await message.channel.send(file=discord.File('5.jpg'))
    if hornopt == 6:
      await message.channel.send(file=discord.File('6.jpg'))
    if hornopt == 7:
      await message.channel.send(file=discord.File('7.jpg'))
    if hornopt == 8:
      await message.channel.send(file=discord.File('8.jpg'))
    if hornopt == 9:
      await message.channel.send(file=discord.File('9.jpg'))
    if hornopt == 10:
      await message.channel.send(file=discord.File('10.jpg'))
    if hornopt == 11:
      await message.channel.send(file=discord.File('11.jpg'))
    if hornopt == 12:
      await message.channel.send(file=discord.File('12.jpg'))
  #
  #
  #
  #
  if message.content.startswith("^horny"):
    iruopt = random.randint(1, 6)
    if iruopt == 1:
      await message.channel.send(file=discord.File('irumean.jpg'))
    if iruopt == 2:
      await message.channel.send(file=discord.File('irumean2.jpg'))
    if iruopt == 3:
      await message.channel.send(file=discord.File('irumean3.jpg'))
    if iruopt == 4:
      await message.channel.send(file=discord.File('irumean4.jpg'))
    if iruopt == 5:
      await message.channel.send(file=discord.File('irumean5.jpg'))
    if iruopt == 6:
      await message.channel.send(file=discord.File('irumean6.jpg'))


keep_alive()
client.run(os.environ['token'])
