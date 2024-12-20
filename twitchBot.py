import asyncio
from twitchio.ext import commands
from datetime import datetime
import pytz


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            token=' xxxx ',                             # xxxx - Replace with your Twtich Auth TOKEN generated at twitchtokengenerator.com
            prefix='!',
            initial_channels=[' xxxx ']                 # xxxx - Replace with the streamer's channel name (not the URL, just the nickname)
        )

    async def event_ready(self):
        print(f"Bot {self.nick} is ready and connected to the chat")
        asyncio.create_task(self.time_announcer())

    async def time_announcer(self):
        poland_tz = pytz.timezone('Europe/Warsaw')      # Set the time zone to Warsaw (Europe/Warsaw)
        while True:
            now = datetime.now(poland_tz).strftime("It's %H:%M")
            for channel in self.connected_channels:
                await channel.send(now)
            await asyncio.sleep(120)                    # Wait for 120 seconds before sending the time again 


# Run the bot
if __name__ == "__main__":
    bot = Bot()
    asyncio.run(bot.run())
