import hikari
import lightbulb
import os
import subprocess

plugin = lightbulb.Plugin("Listen")

@plugin.listener(hikari.GuildMessageDeleteEvent)
async def print_messages(event):
    await event.delete(event.listener)

@plugin.listener(hikari.GuildMessageUpdateEvent)
async def print_messages(event):
    await event.respond(event.listener)

@plugin.listener(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent) -> None:
    ...




def load(bot):
    bot.add_plugin(plugin)