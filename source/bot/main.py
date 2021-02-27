from discord.ext.commands import Bot as Base
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

        super().__init__(command_prefix=PREFIX, owner_id=OWNER_ID)
    
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

    async def on_message(self, message):
        pass

bot = Bot()