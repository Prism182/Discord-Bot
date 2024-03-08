import hikari
import lightbulb
import subprocess
import os
import shutil

bot = lightbulb.BotApp(
    "MTE5NzY2MTYzNzE4MDY3NDA4OQ.G218Z0.JV_sizHI4YB4pxq4zNctIruMIfv58cE8bU7mKg",

    default_enabled_guilds=(1197653145745104967, 1215407623378051132),

    intents=hikari.Intents.ALL_UNPRIVILEGED  # Add this
    | 
    hikari.Intents.MESSAGE_CONTENT,        # 
)

bot.load_extensions_from("./extensions")

@bot.command
@lightbulb.command("restartbot", "restarts the bot")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond("Restarting")
    subprocess.run(
        [
        "python", "./Restartbot.py"
        ]
    )

def close():
    #
    #
    #folder_path = "./zipbomb"
    #file_name2 = "./Zipbomb.zip"
    #
    #
    #@bot.command
    #@lightbulb.option("mb", "How large the zip bomb file is times 10", type=int)
    #@lightbulb.command("createzb", "This creates a zip bomb and sends it to you, maximum file size is 100Mb")
    #@lightbulb.implements(lightbulb.SlashCommand)
    #async def zipb(ctx):
    #    if ctx.options.mb <= 10:
    #        await ctx.respond("creating Zipbomb")
    #        if not os.path.exists(folder_path):
    #            os.makedirs(folder_path)
    #        for i in range(0, ctx.options.mb):
    #            file_name = str(i)
    #            file_path = os.path.join(folder_path, file_name + ".txt")
    #            with open(file_path, "w") as f:
    #                f.write(file_name*100000000)
    #        shutil.make_archive("Zipbomb", "zip", folder_path)
    #        shutil.copyfile(folder_path, "Zipbomb.zip")
    #        await ctx.respond("Zip file created; sending Zip file")
    #        with open("./Zipbomb.zip", "rb") as f:
    #            await ctx.respond(file=hikari.File(f))
    #    else:
    #        await ctx.respond("Please try again as the entered amount is too large")
    return

bot.run()