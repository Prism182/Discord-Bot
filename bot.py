import hikari
import lightbulb
import subprocess
import os
import asyncio
import datetime
import zipfile
import random

bot = lightbulb.BotApp(
    "MTE5NzY2MTYzNzE4MDY3NDA4OQ.G218Z0.JV_sizHI4YB4pxq4zNctIruMIfv58cE8bU7mKg",

    default_enabled_guilds=(1197653145745104967, 1215407623378051132, 1214615652648747048),

    intents=hikari.Intents.ALL_UNPRIVILEGED  # Add this
    | 
    hikari.Intents.MESSAGE_CONTENT,        # 
)

bot.load_extensions_from("./extensions")

@bot.command
@lightbulb.command("restartbot", "restarts the bot")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond("[RESTART SEQUENCE INITIATED]")
    await asyncio.sleep(0.1)
    await ctx.edit_last_response("[DEPLOYING TASM CORRUPTION COUNTERMEASURES]")
    await asyncio.sleep(0.1)
    await ctx.edit_last_response("[RESTARTING][#---------]")
    await ctx.edit_last_response("[RESTARTING][###-------]")
    await ctx.edit_last_response("[RESTARTING][#####-----]")
    await ctx.edit_last_response("[RESTARTING][########--]")
    await ctx.edit_last_response("[RESTARTING][##########]")
    await ctx.edit_last_response("[RESTARTED]")
    subprocess.run(
        [
        "python", "./Restartbot.py"
        ]
    )

@bot.command
@lightbulb.option("channel_name", "the channel id in which you want to purge", type=str)
@lightbulb.option("days", "sets how many days worth of messages you want to delete 0 = today", type=int)
@lightbulb.option("limit", "how many max messages to delete", type=int)
@lightbulb.command("purge-messages", "purges all messages within the channel it is used")
@lightbulb.implements(lightbulb.SlashCommand)
async def purge_messages(ctx):
    if ctx.options.channel_name == "tasm-test" or ctx.options.channel_name == "tasm-testing-grounds":
        channel_id = 1215410347108995072
    elif ctx.options.channel_name == "admin" or ctx.options.channel_name == "admin-bot-commands":
        channel_id = 1197655039657902100
    elif ctx.options.channel_name == "general":
        channel_id = 1197653146219069611
    elif ctx.options.channel_name == "bot-commands":
        channel_id = 1197654649222729768
    elif ctx.options.channel_name == "memes":
        channel_id = 1198026016950595664
    elif ctx.options.channel_name == "help":
        channel_id = 1198026541842567270
    else:
        pass
    await ctx.respond("[PURGE SEQUENCE INITIATED]")
    await ctx.edit_last_response("[DATA PURGE COMMENCING]")
    messages = (
        await bot.rest.fetch_messages(channel_id) # Limit the messages to the specific channel you want to delete from
        .take_until(lambda m: datetime.datetime.now(datetime.timezone.utc) == datetime.timedelta(ctx.options.days)) # Limit the messages to how many days from today you want to purge
        .limit(ctx.options.limit) # Limit the messages to the amount you want deleted
    )
    await bot.rest.delete_messages(channel_id, messages)

file_name = "purger"
folder_path = "./purge"
file_path = os.path.join(folder_path, file_name + ".txt")
folder_to_archive = "./messagelogs"
output_path = "./purger/archive.zip"
user = 741670077128245300
dmcahnnel = 1216008569539924079

@bot.listen(hikari.DMMessageCreateEvent)
async def on_dm_int(event):
    global response
    if event.message.author.id != user and not event.message.author.is_bot:
        channel_id = 1216008569539924079
        channel = await event.app.rest.fetch_channel(channel_id)
        response = random.randint(1, 100000000000000000)
        await channel.send(f"someone has tried to bypass your authorisation, user Id:{event.message.author.id}, Username: {event.message.author.username}, set logs pasword to {response}")
    elif event.message.author.id == user:
        response = event.message.content
    return response

@bot.command
@lightbulb.option("scn", "this is a code that is updated on every use", type=str)
@lightbulb.command("archive-logs", "this deletes all logs from the message logs folder")
@lightbulb.implements(lightbulb.SlashCommand)
async def purge_logs(ctx,):
    await ctx.respond("[IDENTIFYING LIFEFORM]")
    if ctx.options.scn != response:
        await ctx.edit_last_response(f"[Invalid credentials][activativation sequence activated; Code: termination][requestion authorisation]")
        await asyncio.sleep(1)
        await ctx.edit_last_response(f"[authorisation authorisation failed][error code: 401] continuing to monitor specimens")
    elif ctx.options.scn == response:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        with open(file_path, "a") as p:
            current_datetime = datetime.datetime.now()
            time_string = current_datetime.strftime("%H:%M:%S")
            p.write(f'initiated the purge of message logs on {time_string} \n')
        subprocess.run(
            [
                "python", "./purge_message_logs.py"
            ]
        )
        response = random.randint(1, 100000000000000000)

credentials = """
invalid credentials
if you are sure you should have access to this command contact @prism182 for help
if the above is not working for various reasons(prism182 is on holiday, not resopnding etc) please open an issue
to do this use /report-issue command and fill out the form"""

@bot.command
@lightbulb.option("user", "selects a user to pet", type=hikari.Member)
@lightbulb.command("pet", "allows you to pet a member of the server")
@lightbulb.implements(lightbulb.SlashCommand)
async def pet(ctx):
    await ctx.respond(f"{ctx.options.user.mention} has been pet")

bot.run()