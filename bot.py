import discord
from discord.ext import commands

bot = commands.bot(command_prefix='[')

@bot.event
async def on_ready():
    print("bot is online")

bot.run("OTA2Nzk3ODEwMzQ1NzIxODg2.YYd3RQ.Io7WfBlzXwQoH6sdLVljhgIsjGY")