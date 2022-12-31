import discord
import os
TOKEN = '{YOUR TOKEN}'
SERVERID = '{YOUR SERVERID}'
CHANNELID = '{YOUR CHANNELID}'

def run_bot(notification):
    try:
        client = discord.Client(intents=discord.Intents.default())
        @client.event
        async def on_ready():
            server = client.get_guild(int(SERVERID))
            channel = server.get_channel(int(CHANNELID))
            await channel.send("```"+notification+"```")
            await client.close()
        client.run(TOKEN)
    except:
        print("Unable to Send Discord Message")
