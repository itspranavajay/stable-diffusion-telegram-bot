from pyrogram import Client, filters
from pyrogram.types import *
import os
import json
import requests
import io
import random
from dotenv import load_dotenv
from PIL import Image, PngImagePlugin
import base64


load_dotenv()
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
TOKEN = os.getenv("TOKEN")
SD_URL = os.getenv("SD_URL")



bot = Client(
    "stable",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN
)

@bot.on_message(filters.command(["draw"]))
def draw(client, message):
    msgs = message.text.split(' ', 1)
    if len(msgs) == 1:
        message.reply_text("Format : /draw < text to anime image >")
        return
    msg = msgs[1]

    K = message.reply_text("Please Wait 10-15 Second")

    payload = {
        "prompt": msg,
        "steps": 35
        "enable _hr': false,
        "denoising_strength": 0,
        "firstphase_width": 0,
        "firstphase_height": 0,
        "styles": [
            "string"
        ],
        "seed": -1,
        "subseed": -1,
        "subseed_strength": 0,
        "seed_resize_from_h: -1,
        "seed_resize_from_w": -1,
        "batch_size": 1
        "n_iter": 1,
        "steps": 50,
        "cfg scale": 7
        "width": 512,
        "height": 512,
        "restore_faces": false,
        "tiling": false,
        "negative prompt": "string",
        "eta": O,
        "s_churn": 0,
        "s_tmax": 0,
        "s_tmin": 0,
        "s_noise": 1,
        "sampler_ index": "Euler"

    }

    r = requests.post(url=f'{SD_URL}/sdapi/v1/txt2img', json=payload).json()

    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chars1 = "1234564890"
    gen1 = random.choice(chars)
    gen2 = random.choice(chars)
    gen3 = random.choice(chars1)
    gen4 = random.choice(chars)
    gen5 = random.choice(chars)
    gen6 = random.choice(chars)
    gen7 = random.choice(chars1)
    gen8 = random.choice(chars)
    gen9 = random.choice(chars)
    gen10 = random.choice(chars1)
    word = f"{message.from_user.id}-MOE{gen1}{gen2}{gen3}{gen4}{gen5}{gen6}{gen7}{gen8}{gen9}{gen10}"

    for i in r['images']:
        image = Image.open(io.BytesIO(base64.b64decode(i.split(",", 1)[0])))

        png_payload = {"image": "data:image/png;base64," + i}
        response2 = requests.post(url=f'{SD_URL}/sdapi/v1/png-info',
                                  json=png_payload)

        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text("parameters", response2.json().get("info"))
        image.save(f'{word}.png', pnginfo=pnginfo)

        message.reply_photo(
            photo=f"{word}.png",
            caption=
            f"Prompt - **{msg}**\n **[{message.from_user.first_name}-Kun](tg://user?id={message.from_user.id})**\n"
        )
        os.remove(f"{word}.png")
        K.delete()


@bot.on_message(filters.command(["start"], prefixes=["/", "!"]))
async def start(client, message):
    Photo = "https://media.discordapp.net/attachments/1028156834944655380/1062018608022171788/3aac7aaf-0065-40aa-9e4d-430c717b3d87.jpg"

    buttons = [[
        InlineKeyboardButton("Add to your group",
                             url="http://t.me/botname?startgroup=true"),
    ]]
    await message.reply_photo(
        photo=Photo,
        caption=
        f"Hello! I'm botname Ai and I can make an anime-styled picture!\n\n/draw text to anime image",
        reply_markup=InlineKeyboardMarkup(buttons))


bot.run()
