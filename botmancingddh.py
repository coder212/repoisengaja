#dibuat oleh john thor 
#kalo mau pake ya pake aja sih kalo pengen mau ngembangin juga silakan
#yang jelas ini source code hanyalah asal ketik
#library yan diperlukan adalah telethon sisanya udah bawaan dan aku mengunakan bot ini dengan python3.5
import os, re, random, asyncio, sys, time, json
from telethon import TelegramClient, events, sync
def read_the_env():
   f = open("env.json","r+")
   text= f.read()
   f.close()
   return text

configjson = json.loads(read_the_env()) 
API_ID = configjson['api_id']
API_HASH = configjson['api_hash']
client = TelegramClient('makun', API_ID, API_HASH)
dest= 'danaudalamhutan'

async def nungguin(w):
   await asyncio.sleep(w*60)

async def mancingddh(client,w):
   while True:
       await client.send_message(dest, "/fish")
       await nungguin(w)

#@client.on(events.NewMessage(incoming=True, from_users=dest))
#async def handle_chat(event):
#   message = event.raw_text
#   print(message)
#   if "halo" in message:
#      await client.send_message(dest, "oh iya")
#   else:
#      a= random.randint(0, len(jrandom)-1)
#      print("response: {}".format(jrandom[a]))
#      await client.send_message(dest, jrandom[a])

with client:
   client.loop.create_task(mancingddh(client,8))
   client.run_until_disconnected()
