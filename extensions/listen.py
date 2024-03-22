import hikari
import lightbulb
import os
import datetime
from datetime import date
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

plugin = lightbulb.Plugin("Listen")

logger_path = "./messagelogs"

@plugin.listener(hikari.GuildMessageCreateEvent)
async def welcome(event):
    if hikari.MessageCreateEvent.channel_id == 1214615653223505973:
        await event.create_message(1214615653223505973, f"Welcome mortal... {hikari.User.mention}{event.message.author.username}")
        await event.create_message(1214615653223505973, "It seems as though you have joined this sanction though means unknown")
        await event.create_message(1214615653223505973, "This has been recored to the archives")
        await event.create_message(1214615653223505973, "Now I will tell you this once")
        await event.create_message(1214615653223505973, "If you want to be forgiven i will suggest one thing, and one thing alone")
        await event.create_message(1214615653223505973, "**LEAVE**")

@plugin.listener(hikari.MessageCreateEvent)
async def print_messages_to_txtfile(event):
    if not event.message.author.is_bot:
        if not os.path.exists(logger_path):
            os.makedirs(logger_path)
        file_name = str(date.today())
        file_path = os.path.join(logger_path, file_name + ".txt")
        logger.info(f'Message from {event.message.author.username}: "{event.message.content}" in channel with id: {event.message.channel_id}')
        with open(file_path, "a") as f:
            current_datetime = datetime.datetime.now()
            time_string = current_datetime.strftime("%H:%M:%S")
            f.write(f'Message from {event.message.author.username}: "{event.message.content}" in channel with id: {event.message.channel_id} at the time of {time_string} \n')

@plugin.listener(hikari.MessageUpdateEvent)
async def print_messages_to_txtfile(event):
    if not os.path.exists(logger_path):
        os.makedirs(logger_path)
    if not event.message.author.is_bot:
        file_name = str(date.today())
        file_path = os.path.join(logger_path, file_name + ".txt")
        logger.info(f'A message from {event.message.author.username} was updated to: "{event.message.content}" in channel with id: {event.message.channel_id}')
        with open(file_path, "a") as f:
            current_datetime = datetime.datetime.now()
            time_string = current_datetime.strftime("%H:%M:%S")
            f.write(f'A message from {event.message.author.username} was updated to: "{event.message.content}" in channel with id: {event.message.channel_id} at the time of {time_string} \n')

@plugin.listener(hikari.GuildMessageUpdateEvent)
async def message_edit_logger(event):
    pass
@plugin.listener(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent) -> None:
    pass

def load(bot):
    bot.add_plugin(plugin)