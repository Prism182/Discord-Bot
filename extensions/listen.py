import hikari
import lightbulb
import os
import subprocess

plugin = lightbulb.Plugin("Listen")

@plugin.listener(hikari.GuildMessageDeleteEvent)
async def print_messages(event):
    pass

@plugin.listener(hikari.GuildMessageUpdateEvent)
async def message_edit_logger(event):
    pass
@plugin.listener(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent) -> None:
    ...

def load(bot):
    bot.add_plugin(plugin)