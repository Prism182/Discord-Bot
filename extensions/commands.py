import hikari
import lightbulb
import os
import subprocess
import asyncio
import time

plugin = lightbulb.Plugin("Commands")


@plugin.command
@lightbulb.command("ping", "says pong! and tells the user how fast the bot responded")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    start_time = time.monotonic()
    await ctx.respond("Pong!")
    end_time = time.monotonic()
    response_time = round((end_time - start_time)* 1000, 2)
    await ctx.edit_last_response(f"Pong! Response time:{response_time}ms")

#@plugin.command
#@lightbulb.command("group", "this is a group")
#@lightbulb.implements(lightbulb.SlashCommandGroup)
#async def my_group(ctx):
#    pass

#@my_group.child
#@lightbulb.command("issue", "this is a subcommand")
#@lightbulb.implements(lightbulb.SlashSubCommand)
#async def subcommand(ctx):
#    await ctx.respond("I am a subcommand")

#@plugin.command
#@lightbulb.option("num2", "the second number", type=int)
#@lightbulb.option("num1", "the first number", type=int)
#@lightbulb.command("add", "Add two numbers together")
#@lightbulb.implements(lightbulb.SlashCommand)
#async def add(ctx):
#    await ctx.respond(ctx.options.num1 + ctx.options.num2)

@plugin.command
@lightbulb.command("ip", "tells you the current IP of the server (not likely to change)")
@lightbulb.implements(lightbulb.SlashCommand)
async def ip(ctx):
    await ctx.respond("the current IP of the server is 1.1.1.1:1111")

@plugin.command
@lightbulb.command("startvanillaserver", "Starts up the server!")
@lightbulb.implements(lightbulb.SlashCommand)
async def startserver(ctx):
    await ctx.respond("starting up the server")
    await asyncio.sleep(1)
    subprocess.run(
        [ 
            "python",  ".\Extra\RunVanillaServer.py"
        ]
    )
    await asyncio.sleep(5)
    await ctx.respond("The server has been stopped (stopped by admin or it has crashed)")

@plugin.command
@lightbulb.command("startspigotserver", "Starts up the server!")
@lightbulb.implements(lightbulb.SlashCommand)
async def startserver(ctx):
    await ctx.respond("starting up the server")
    await asyncio.sleep(1)
    subprocess.run(
        [ 
            "python",  ".\Extra\RunSpigotServer.py"
        ]
    )
    await asyncio.sleep(5)
    await ctx.respond("The server has been stopped (stopped by admin or it has crashed)")

@plugin.command
@lightbulb.command("serverhelp", "displays the names and uses of all the commands")
@lightbulb.implements(lightbulb.SlashCommand)
async def help(ctx):
    await ctx.respond(help_command)

help_command = """
Commands:
"/ping" - this is to check if the bot is alive, will respond with pong if yes, nothing if no
"/ip" - this tells you the current ip of the server, this is unlikely to change
"/startvanillaserver" - this starts up the vanilla server
"/startspigotserver" - this starts up the spigot server
"/serverhelp" - displays this menu
more commands are coming as nessisary 
"""

@plugin.command
@lightbulb.command("report-issue", "sends a link to the issues tracker for the bot")
@lightbulb.implements(lightbulb.SlashCommand)
async def help(ctx):
    await ctx.respond(issue)

issue = """
To report an issue or change please go to the following link and apply the labels "Bug" or "Enhancement" approprietly,
https://github.com/Prism182/Discord-Bot/issues/new
For major issues, (the bot crashes when you run a script, the bot does not communicate)Please use the Issue tracker and then ping @Prism182 for more help
"""

@plugin.command
@lightbulb.command("startup", "starts up prism.exe")
@lightbulb.implements(lightbulb.SlashCommand)
async def run(ctx):
    subprocess.run(
        [
            "python", "PSS.py"
        ]
    )

def load(bot):
    bot.add_plugin(plugin)