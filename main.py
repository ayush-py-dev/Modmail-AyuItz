from discord.ext import commands
import discord
import os,keep_alive

intents = discord.Intents.default()
# we need members intent too
intents.members = True

bot = commands.Bot(command_prefix = "==", intents = intents)

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Dms in Ayu Itz"))
  print("Bot logged in!")
  bot.load_extension("cogs.onMessage")



keep_alive.keep_alive()
bot.run(os.environ.get("TOKEN"))