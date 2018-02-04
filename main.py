from pprint import pprint
import json
import sys
import requests
import apis as api
import html

url = 'http://localhost:80/parse'
min_confidence = 0.65

def makeRequest(message_body):
  payload = {"q": message_body}
  r = requests.get(url, params=payload)
  return r.json()

def handleRequest(classified_text):
  intent = classified_text['intent']['name']
  confidence = classified_text['intent']['confidence']
  entities = classified_text['entities']

  if confidence < min_confidence:
    return no_confidence()
  if intent == "get_weather":
    return get_weather(entities)
  elif intent == "get_news":
    return get_news(entities)
  elif intent == "get_directions":
    return get_directions(entities)
  elif intent == "get_what":
    return get_what()
  elif intent == "greet":
    return greet()
  elif intent == "get_translation":
    return get_translation(entities)
  else:
    return no_confidence()

def get_what():
  return ("Hi! I'm Mr. WorldWide, a travel helper bot. You can text me from SMS and not use your data while your travelling.\nThis is what I can help you with:\n* Weather\n* News\n* Directions\n* Translation")

def greet():
  return ( "Hi! I'm Mr. WorldWide, a travel helper bot. Dallé!")

def get_weather(entities):
  found = False
  for candidate in entities:
    if candidate['entity'] == 'city':
      location = candidate['value']
      found = True
      break
  if found:
    return (api.getWeather(location))
  else:
    no_confidence()

## Can probably abstract away
def get_news(entities):
  found = False

  for candidate in entities:
    if candidate['entity'] == 'city':
      location = candidate ['value']
      found = True
      break
  if found:
    string = html.unescape(api.getNews(location))
    string = string[:10]
    return html.unescape(api.getNews(location))
  else:
    no_confidence()

def get_translation(entities):
  found = False
  found2 = False

  for candidate in entities:
    if candidate['entity'] == 'language':
      language = candidate ['value']
      found = True
      break
  
  for candidate in entities:
    if candidate['entity'] == 'text_to_translate':
      text_to_translate = candidate ['value']
      found2 = True
      break

  if found and found2:
    return (html.unescape(api.translate(text_to_translate, language)))
  else:
    no_confidence()


def get_directions(entities):
  found = False
  found2 = False
  found3 = False

  for candidate in entities:
    if candidate['entity'] == 'origin':
      origin = candidate ['value']
      found = True
      break
  
  for candidate in entities:
    if candidate['entity'] == 'destination':
      destination = candidate ['value']
      found2 = True
      break
  
  for candidate in entities:
    if candidate['entity'] == 'method_of_transport':
      mode = candidate ['value']
      found3 = True
      break
  
  if found and found2 and not found3:
    return (api.getDirections(origin, destination, "transit"))
  elif found and found2 and found3:
    return (api.getDirections(origin, destination, mode))
  else:
    return no_confidence()
  
def no_confidence():
  ##TODO:Expand it
  return ("I'm sorry but I don't know what you mean! Can you try rephrasing it?")

def main(message_body):
  classified_text = makeRequest(message_body)
  pprint (classified_text)
  return handleRequest(classified_text)
