import os
import discord
from python_aternos import Client
from time import sleep
import sys

def check_server_status():
    bot = Client.from_credentials("Mr_ater","ra12ra23")
    server = bot.list_servers()[0]
    if server.status == "offline":
        print("Server is offline")

        return False
    else:
        print("Server is online")

        return True
    
def start_server():
    bot = Client.from_credentials("Mr_ater","ra12ra23")
    server = bot.list_servers()[0]
    if server.status == "online":
        print("Server is already online")
        return False
    else:
        server.start()
        print("Starting server...")
        return True

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    print(f"Bot has been started, you can use it now")

@client.event
async def on_message(message):
    print(message.content)
    if message.content == "!status":
        while True:
            if check_server_status():
                await message.channel.send("Bot server is online")
      
                break
            else:
                await message.channel.send("Bot server is offline")
  
                break
    elif message.content == "!startserver":
        if start_server():
            await message.channel.send("Starting the server. Please wait...")
            sleep(30)
            while True:
                if check_server_status():
                    await message.channel.send("Server is now online!")
                    break
                else:
                    await message.channel.send("Server is still starting...")
                    sleep(30)
                    continue
        else:
            await message.channel.send("The server is already online!")
          

client.run("MTEwMzI1OTM2ODYxNjY0MDU0NA.GiTbMa.KniiVkKqT4egj3JGwvj-0XNYxqgdjyLb73th8k")
