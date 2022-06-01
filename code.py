## Robert ##

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

## Other ##

def confused(text, state):
  return "I don't know who I am..."

def hello(text, state):
  return "Hello, my name is Robert."

def echo(text, state):
  return 'You said "%s."' % text
