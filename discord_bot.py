import os
from decimal import Decimal
import discord
from discord.ext import commands
from dotenv import load_dotenv
from utils.orders import send_order_request
from utils.account_assets import get_upbit_assets

from services.get_coint_price import get_price

load_dotenv(override=True)

intents = discord.Intents.default()
intents.message_content = True  # 메시지 내용을 읽을 수 있는 권한 추가

bot = commands.Bot(intents=intents, command_prefix="!")


@bot.event
async def on_ready():
    print(f"Login bot: {bot.user}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    print(message.author)
    if message.content.startswith("!BUY"):
        if "KRW" in message.content:

            market = message.content[message.content.find("KRW") :]
            res = send_order_request(
                market=market, side="bid", ord_type="price", price="5000"
            )
    if message.content.startswith("!SELL"):
        if "KRW" in message.content:
            market = message.content[message.content.find("KRW") :]

            my_assets = get_upbit_assets()
            for asset in my_assets:
                if asset["currency"] == market.split("-")[1]:
                    print(asset["balance"])
                    coin_amount = float(5000 / get_price(market))
                    amount = str("{:.5f}".format(round(float(coin_amount), 5)))
                    print(amount)
                    res = send_order_request(
                        market=market, side="ask", ord_type="market", volume=amount
                    )
    await message.channel.send(res)

    await bot.process_commands(message)


@bot.command()
async def BUY(message):
    pass


@bot.command()
async def SELL(message):
    pass


@bot.command()
async def tick_list(message):
    from services.get_list import get_minute_candle_list

    tick_list = get_minute_candle_list()

    cnt = 0
    for tick in tick_list:
        import json

        await message.channel.send(json.dumps(tick, indent=4))
        cnt += 1
        if cnt == 5:
            break


@bot.command()
async def hello(message):
    print("hello")
    await message.channel.send("Hi!")


bot.run(os.environ["DISCORD_BOT_TOKEN"])
