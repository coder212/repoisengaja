#dibuat oleh john thor 
#kalo mau pake ya pake aja sih kalo pengen mau ngembangin juga silakan
#yang jelas ini source code hanyalah asal ketik
#library yang diperlukan adalah telethon sisanya udah bawaan dan aku mengunakan bot ini dengan python3.5
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

dest= ('danaudalamhutan','kampungmaifambot')


async def nungguin(w):
   await asyncio.sleep(w)


async def bertani(client,w, tanaman, lahan):
   while True:
       await client.send_message(dest[1], "/panen")
       await nungguin(1)
       await client.send_message(dest[1], "/tanam_{}_{}".format(tanaman, lahan))
       await nungguin(1)
       await client.send_message(dest[1], "/siram")
       await nungguin(w)

async def mancingddh(client,w):
   while True:
       await client.send_message(dest[0], "/fish")
       await nungguin(w)

async def cekstatus(client,w):
   while True:
       await client.send_message(dest[1], "/status")
       await nungguin(w)

@client.on(events.NewMessage(incoming=True, from_users=dest))
async def handle_chat(event):
   message = event.raw_text
   print(message)
#   if "halo" in message:
#      await client.send_message(dest, "oh iya")
#   else:
#      a= random.randint(0, len(jrandom)-1)
#      print("response: {}".format(jrandom[a]))
#      await client.send_message(dest, jrandom[a])

with client:
   #client.loop.create_task(mancingddh(client,480))
   #client.loop.create_task(bertani(client,300,"cabai",143))
   client.loop.create_task(cekstatus(client,300))
   client.run_until_disconnected()
