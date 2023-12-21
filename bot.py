import yaml
import discord
import socket

with open('config.yaml', 'r') as file:
  config = yaml.safe_load(file)

token = config["token"]
do_sprawdzenia = config["do_sprawdzenia"]
port = config["port"]
gid = config["serwery"]

bot = discord.Bot()

@bot.command(description="Wysyła ping bota.")
async def ping(ctx):
  await ctx.respond(f"Ping bota wynosi {bot.latency}")

@bot.command(description="Wysyła ping bota.")
async def github(ctx):
  await ctx.respond(f"Ten bot jest w pełni Open Source. Jego kod możesz znaleźć [tutaj](https://github.com/szewczuko/infotechmc-discord)")

@bot.command(guild_ids=gid, name = "status", description="Sprawdza czy serwer jest dostępny")
async def status(ctx):
  await ctx.defer()
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    s.connect((do_sprawdzenia, port))
    await ctx.respond(f"Serwer MC jest dostępny.")

  except socket.error as e:
    await ctx.respond(f"Serwer minecraft jest offline.")

  finally:
    s.close()


bot.run(token)
