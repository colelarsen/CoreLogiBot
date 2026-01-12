# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
from main import download_image
from main import send_image
from main import delete_file
from google_sheet import authentication_sheets
from google_sheet import update_values
from adapter import stock_json_to_sheet_data
from main import update_differences_in_sheet
import traceback


IMAGE_FILE = "image_to_process.png"

def setup():
    authentication_sheets()

    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix='$', intents=intents)

    @bot.command()
    async def testercole(ctx):
        pass

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('$update'):
            try:
                stockpile = message.content.split(": ")[1]

                if len(message.attachments) != 0:
                    print(message.attachments[0].url)
                    download_image(message.attachments[0].url, IMAGE_FILE)
                    jsonresponsestring = send_image(IMAGE_FILE)
                    delete_file(IMAGE_FILE)

                    sheet_list = stock_json_to_sheet_data(jsonresponsestring)
                    update_values(sheet_list, stockpile=stockpile)

                    response = update_differences_in_sheet(stockpile)


                    await message.channel.send(response)
            except Exception as e:
                await message.channel.send(str(traceback.format_exc()))

    client.run('DISCORD API KEY GOES HERE')

setup()