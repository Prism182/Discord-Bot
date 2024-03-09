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
    ...

def load(bot):
    bot.add_plugin(plugin)