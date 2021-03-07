from discord.ext.commands import Cog

class Random(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @Cog.listener()
    async def on_ready(self):
        pass

def setup(bot):
    bot.add_cog(Random(bot))
