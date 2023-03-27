# bot.py
# Handles user commands and messages.

import discord
import ape_handler
import message_reader
def run_discord_bot(TOKEN, APE_KEY):
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents = intents)

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('!'):
            #request  (TUPLE) = message_reader.process_request(message.content[1:])
            #response (DICT) = ape_handler.generate_response(APE_KEY, request)
            #message  (STR) = ape_reader.process_response(response)
            #await message.channel.send(message)
            pass
    client.run(TOKEN)