from discord.ext.commands import Bot as Base
from discord.ext.commands import CommandNotFound
from discord import Intents
from discord import Embed
from apscheduler.schedulers.asyncio import AsyncIOScheduler
# Prefix for chat commands
PREFIX = "."
# User ID from Discord
OWNER_ID = [305379360452640778]
# Guild (server) ID from Discord
GUILD_ID = 528544644678680576

class Bot(Base):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        super().__init__(
            command_prefix=PREFIX, 
            owner_id=OWNER_ID, 
            intents=Intents.all(),
        )
    
    def run(self):
        with open("./config/TOKEN.txt", "r", encoding="utf-8") as token_file:
            self.TOKEN = token_file.read()

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