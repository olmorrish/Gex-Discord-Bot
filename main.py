import discord
import os
import random

client = discord.Client() #register a client

message_chance = 1

reference_formats = [
"This reminds me of <EVENT> at <PERSON>'s .",
"Note to self: don't <ACTION> at <PERSON>'s.",
"This is just like <ACTION-ING> at <PERSON>'s house.",
"This comment reminds me of <ACTION-ING> in <PERSON>'s <LOCATION>.",
"This is just like <EVENT> at <PERSON>'s house.",
"Reminds me of <PERSON>'s <LOCATION>.",
"I haven't been this <EMOTION> since I was stuck at <EVENT> at <PERSON>'s.",
"Last time I was this <EMOTION>, I was <ACTION-ING> at <PERSON>'s.",
"Last time I was this <EMOTION>, I was <ACTION-ING> in <PERSON>'s <LOCATION>.",
"This comment is <ADJ-ER> than <EVENT> at <PERSON>'s.",
"This comment is <ADJ-ER> than <EVENT> in <PERSON>'s <LOCATION>."
]

celebrities = ["Winona Ryder","Sarah Michelle Gellar","Whitney Houston","Cher","John Travolta","Charlie Sheen","George Clooney","Drew Carey","Macauley Culkin","Joe Pesci","Daniel Stern","John Candy","Tim Curry","Brendan Fraser","Rachel Weisz","Clancy Brown","Sigourney Weaver","Ron Perlman","Ernie Hudson","Rick Moranis","Harold Ramis","Al Pacino","Daniel Day-Lewis","Kevin Costner","Meg Ryan","Jeff Bridges","John Malkovich","Michael Douglas","Uma Thurman","Jim Carrey","Geena Davis","Antonio Banderas","Kathy Bates","Anjelica Huston","Adam Sandler","Richard Simmons","Tim Burton","Don Cheadle","Rip Taylor","Tom Green","Drew Barrymore","James Earl Jones","Jackie Chan","Jerry Garcia","Cameron Diaz","Rowan Atkinson","Guy Fieri"]

adjectives_er = ["scarier","weirder","more boring","stranger","funnier","better thought out","better planned","easier to digest","easier to wrap my head around","more haywire","more enlightening","more mysterious","better","cooler","quieter"]

#I haven't been this..._____
emotions = ["frightened","scared","upset","surprised","depressed","tired","confused","aroused"]

#this reminds me of..._____
actions_ing = ["playing skiball","playing bingo","watching baseball","drinking whiskey","having a snowball fight","eating corn chips","playing high-stakes poker","listening to vintage records","bungee jumping","binge drinking","cooking meatloaf","arm-wrestling","setting off fireworks","playing charades","using the bathroom","salsa dancing"]

#dont..._____
actions_past = ["drink tap water","play bingo","watch Fraser","get into a fight","eat finger food","play blackjack","play soft jazz","bare-knuckle box","cook meatloaf","flush","look into the mirrors","turn on the ceiling fans","make eye contact with the guests","call the police","talk politics","start fires"]

locations = ["vacation home","bathroom","rumpus room","ball pit","garage","basement","wine cellar","favourite restaurant","pantry","powder room","home theater","attic","crawl space"]

events = ["a luau","a bar mitzvah","an all-nighter","Halloween night","Christmas Eve","New Year's","taco night","a Murdoch Mysteries watch party","a pizza party","poker night","Saint Patrick's Day","Valentine's Day","a Superbowl party","Dungeons and Dragons","a wedding","a funeral","networking seminars","night classes","Russian roulette"]

@client.event 
async def on_ready(): #called when bot is ready to start
  print('We have logged in as {0.user}'.format(client))
  game = discord.Game("Knack 2")
  await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
  if(message.author == client.user):
    return

  rand = random.uniform(0.1,100.0);
  print("Random number: ",rand)

  if(rand <= message_chance):

    #generate the message
    reference = gen_from(reference_formats)
    print("Using reference: " + reference)

    while("<PERSON>" in reference):
      reference = reference.replace("<PERSON>", gen_from(celebrities))
    while("<ADJ-ER>" in reference):
      reference = reference.replace("<ADJ-ER>", gen_from(adjectives_er))
    while("<EMOTION>" in reference):
      reference = reference.replace("<EMOTION>", gen_from(emotions))
    while("<ACTION-ING>" in reference):
      reference = reference.replace("<ACTION-ING>", gen_from(actions_ing))
    while("<ACTION>" in reference):
      reference = reference.replace("<ACTION>", gen_from(actions_past))
    while("<LOCATION>" in reference):
      reference = reference.replace("<LOCATION>", gen_from(locations))
    while("<EVENT>" in reference):
      reference = reference.replace("<EVENT>", gen_from(events))
    
    await message.reply(reference)

def gen_from(ref_list):
  return ref_list[random.randint(0,len(ref_list)-1)]

client.run(os.environ['envtoken'])