# bot.py
# Handles user commands and messages.
import discord
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
            try:
                bot_message = message_reader.process_request(message.content[1:])
                await message.channel.send(bot_message)
            except message_reader.MessageProcessError:
                await message.channel.send('Your monkey command is incorrect!')

    client.run(TOKEN)