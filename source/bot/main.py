from discord.ext.commands import Bot as Base
from discord.ext.commands import CommandNotFound
from discord import Intents
from discord import Embed
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from ..database import database
import json

# Change your variables in config file
try:
    with open("./config/config.json", "r") as config_file:
        config = json.load(config_file)
        TOKEN = config["@TOKEN@"]
        PREFIX = config["@PREFIX@"]
        OWNER_ID = config["@OWNER_ID@"]
        GUILD_ID = config["@GUILD_ID@"]
except IOError:
    print("Config file was not found.")
    input()
    raise
except KeyError:
    print("Invalid config variable.")
    input()
    raise
except:
    print("An unknown error occured.")
    input()
    raise

class Bot(Base):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        database.autosave(self.scheduler)
        super().__init__(
            command_prefix=PREFIX, 
            owner_id=OWNER_ID, 
            intents=Intents.all(),
        )
    
    def run(self):
        self.TOKEN = TOKEN

        print("Bot is active...")
        super().run(self.TOKEN, reconnect=True)
    
    async def on_connect(self):
        print("Bot is connected.")
    
    async def on_disconnect(self):
        print("Bot is disconnected.")

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(GUILD_ID)
            self.scheduler.start()

            print("Bot is ready.")
        else:
            print("Bot reconnected.")

    #////////// Error Handling ///////////
    async def on_error(self, error, *args, **kwargs):
        if error == "on_command_error":
            await args[0].send("A command error occurred.")
        raise
    
    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            await ctx.send("Wrong command")
        elif hasattr(exc, ["original"]):
            raise exc.original
        else:
            raise exc
    #/////////////////////////////////////

    async def on_message(self, message):
        pass

bot = Bot()