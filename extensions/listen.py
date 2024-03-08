import hikari
import lightbulb
import os
import subprocess

plugin = lightbulb.Plugin("Listen")

@plugin.listener(hikari.GuildMessageDeleteEvent)
async def print_messages(event):
    await event.delete(event.listener)

@plugin.listener(hikari.GuildMessageUpdateEvent)
async def message_edit_logger(event):

    old_message = await event.message.get_old()

    if old_message:
        old_content = event.old_content
        new_content = event.new_content
        channel = event.message.get_channel()
        author = event.message.author

        print(f"Message updated by {author.username}:")
        print(f"Old content: {old_content}")
        print(f"New content: {new_content}")

@plugin.listener(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent) -> None:
    ...

def load(bot):
    bot.add_plugin(plugin)