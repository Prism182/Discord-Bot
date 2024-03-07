import hikari
import lightbulb

bot = lightbulb.BotApp(
    "MTE5NzY2MTYzNzE4MDY3NDA4OQ.G218Z0.JV_sizHI4YB4pxq4zNctIruMIfv58cE8bU7mKg",

    #default_enabled_guilds=(1197653145745104967),

    intents=hikari.Intents.ALL_UNPRIVILEGED  # Add this
    | 
    hikari.Intents.MESSAGE_CONTENT,        # 
)

bot.load_extensions_from("./extensions")

bot.run()