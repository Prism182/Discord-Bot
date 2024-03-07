import hikari
import lightbulb
import os
import subprocess

plugin = lightbulb.Plugin("Listen")

@plugin.listener(hikari.StartedEvent)
async def bot_started(event):
    print("bot has started!")

@plugin.listener(hikari.GuildMessageDeleteEvent)
async def print_messages(event):
    pass

@plugin.listener(hikari.GuildMessageUpdateEvent)
async def print_messages(event):
    pass

@plugin.listener(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent) -> None:
    ...


def load(bot):
    bot.add_plugin(plugin)