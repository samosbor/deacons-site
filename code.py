## Robert ##

import random

def robert(text, state):
  if 'joke' in text.lower():
    state['joke'] = ['What has 18 wheels and flies?', 'A garbage truck.']
  if state.get('joke'):
    return state.get('joke').pop(0)

  facts = [
    "My favorite color is yellow.",
    "I have two sets of twins.",
    "The sun is hot.",
    "Three is a magic number.",
  ]
  random.shuffle(facts)
  used = state.get('used', [])
  for fact in facts:
    if fact not in used:
      used.append(fact)
      state['used'] = used
      return fact
  else:
    return "I'm all out of ideas..."

state = {}
print(robert("", state))
print(robert("joke", state))
print(robert("", state))
print(robert("", state))
print(robert("", state))

## Sam ##

def sam(text, state):
  if 'goat' in text.lower():
    return "I am goated with the sauce"

## Other ##

def confused(text, state):
  return "I don't know who I am..."

def hello(text, state):
  return "Hello, my name is Robert."

def echo(text, state):
  return 'You said "%s."' % text

## beckett

def beckett(text, state):
  if 'i need help bad' in text.lower():
    state['i need help bad'] = ['<a href="https://www.youtube.com/watch?v=GA_2W\
VTQNY0">link</a>']
  if state.get('i need help bad'):
    return state.get('i need help bad').pop(0)

  facts = [
    "bruh.",
    "nancy wheeler is so hot",
    "<img src='https://i.pinimg.com/originals/58/9b/d6/589bd6f5dad99aec4df807549eb8ed6e.jpg'>",
    "Three is a magic number.",
    "<img src='https://assets.reedpopcdn.com/ugly-sonic.png/BROK/thumbnail/1200x900/quality/100/ugly-sonic.png'>"
  ]
  random.shuffle(facts)
  used = state.get('used', [])
  for fact in facts:
    if fact not in used:
      used.append(fact)
      state['used'] = used
      return fact
  else:
    return "kys"


def Cohen (text, state):
  if 'how do you be a baddieeeee' in text.lower():
    state['x'] = ['ME WHEN step on me']
 
  if 'Traderie Giveaway is LIVE - Enter Now on the Traderie Website!' in text:
    state['x'] = ['https://www.youtube.com/watch?v=lmTG5L81GIQ']

  if 'Today, as on the first Wednesday of every month, we’re donating to Breast Cancer Research and treatment through ' in text:
    state['x'] = ['Gurl i dont even use sezan also june!!!!!SHEKANOU HEIZOU🤩🤩🤩']

  if state.get('x'):
    return state.get('x').pop(0)
    
  facts = [
    "Ate and left no crumbs",
    "very very big secret omg",
    "me when xoxo gossip gorl",
    "<img src='https://www.pinterest.com/pin/21181060734329735/'>",
  ]
  random.shuffle(facts)
  used = state.get('used', [])
  for fact in facts:
    if fact not in used:
      used.append(fact)
      state['used'] = used
      return fact
  else:
    return "Aight, ima head to bed"
    ## luke ##

import random

def luke(text, state):
  if 'joke' in text.lower():
    state['joke'] = ['what is smelly?', 'not me that is fur sure.']
  if state.get('joke'):
    return state.get('joke').pop(0)
  if 'backwards' in text.lower():return text [::-1]
  facts = [
    "Beckett is smelly.",
    "i am smelly.",
    "This is me facts.",
    "Pooooooooooooooooooooooooooooo.",
  ]
  random.shuffle(facts)
  used = state.get('used', [])
  for fact in facts:
    if fact not in used:
      used.append(fact)
      state['used'] = used
      return fact
  else:
    return "me gorilla"

state = {}
print(luke("", state))
print(luke("i am a backwards peple", state))
print(luke("", state))
print(luke("", state))
print(luke("", state))


## Conley ##

import random

def Conley(text, state):
  if 'joke' in text.lower():
    state['joke'] = ['Why did the chicken cross the road?', 'To get to the other side.']
  if state.get('joke'):
    return state.get('joke').pop(0)
    
  if 'hi' in text.lower():
    hireplies = [
    "Hello",
    "Hi",
    "Wassup",
    "Yolo",
    "Yeeeeeeeee",
    "goodbye",
    "okay",
    "fine"
    ]
    random.shuffle(hireplies)
    return(hireplies[0])

  smashreplies = [
        "Bayonetta",
        "Bowser",
        "Bowser Jr.",
        "Captain Falcon",
        "Chrom",
        "Cloud",
        "Corrin",
        "Daisy",
        "Dark Pit",
        "Dark Samus",
        "Diddy Kong",
        "Donkey Kong",
        "Dr. Mario",
        "Duck Hunt",
        "Falco",
        "Fox",
        "Ganondorf",
        "Greninja",
        "The Ice Climbers",
        "Ike",
        "Incineroar",
        "Inkling",
        "Isabelle",
        "Jigglypuff",
        "Ken",
        "King Dedede",
        "King K. Rool",
        "Kirby",
        "Link",
        "Little Mac",
        "Lucario",
        "Lucas",
        "Lucina",
        "Luigi",
        "Mario",
        "Marth",
        "Mega Man",
        "Meta Knight",
        "Mewtwo",
        "Mii Brawler",
        "Mii Gunner",
        "Mii Fighter",
        "Mr. Game & Watch",
        "Ness",
        "Captain Olimar",
        "Pac-Man",
        "Palutena",
        "Peach",
        "Pichu",
        "Pikachu",
        "Piranha Plant (DLC)",
        "Pit",
        "Pokemon Trainer (Charizard, Ivysaur and Squirtle)",
        "R.O.B. the robot",
        "Robin",
        "Rosalina",
        "Roy",
        "Richter",
        "Ridley",
        "Ryu",
        "Samus",
        "Sheik",
        "Shulk",
        "Simon Belmont",
        "Solid Snake",
        "Sonic",
        "Toon Link",
        "Villager",
        "Wario",
        "Wii Fit Trainer",
        "Wolf",
        "Yoshi",
        "Young Link",
        "Zelda",
        "Zero Suit Samus",
    ]
  
  random.shuffle(smashreplies)
  return(smashreplies[0])

  facts = [
    "My favorite color is sea green.",
    "I have four siblings",
    "Ice is cool",
    "The Wii is the best Nintendo console.",
  ]
  random.shuffle(facts)
  used = state.get('used', [])
  for fact in facts:
    if fact not in used:
      used.append(fact)
      state['used'] = used
      return fact
  else:
    return "I'm all out of ideas..."
    
    
print(Conley("hi",{}))

print(Conley("what is the best smash character",{}))