from pyrogram import Client, filters
from pyrogram.types import *
import os
import json
import requests

from time import sleep
import string
words = ['nsfw', 'nude', 'naked', 'pussy', 'vagina', 'dick', 'cock', 'penis', 'loli', 'shota', 'child', 'children', 'xnxx', 'pron', 'hentai', 'asshole', 'sex', 'xxxx', 'xxx', 'pronhub', 'boob', 'boobs']
 

import requests

import asyncio, time


TOKEN = os.getenv('TOKEN')
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
key = os.getenv('KEY')

app = Client("Db", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)



@app.on_callback_query()
async def model_callback_data(client, callback_query: CallbackQuery):
    Data = callback_query.data
    message = callback_query.message
    Kn = Data.split("_")
    action = Kn[0]
    user = Kn[1]
    userid = Kn[1]
    

    await callback_query.answer()

    to_animejourney = False
    to_anything = False
    to_midjourney = False
    to_deliberate = False
    to_dosmix = False   
    to_chilloutmix = False
    to_dreamshaper = False
    to_counterfeit = False
    to_meinamix = False
    to_real = False
    to_model = False
    to_reals = False
    to_animev1 = False
    to_animev2 = False

    if action == "square":
        to_real = True
    elif action == "landscape":
        to_model = True
    elif action == "portrait":
        to_reals = True
    

    elif action == "animejourney":
        to_animejourney  = True
    elif action == "anythingv3":
        to_anything = True
    elif action == "midjourney":
        to_midjourney = True
    elif action == "deliberate":
        to_deliberate = True
    elif action == "dosmix":
        to_dosmix = True
    elif action == "chilloutmix":
        to_chilloutmix = True
    elif action == "dreamshaper":
        to_dreamshaper = True
    elif action == "counterfeit":
        to_counterfeit = True
    elif action == "meinamix":
        to_meinamix = True
      
    
    
    else:
        return

    chatid = callback_query.message.chat.id
    r = message.text
    texts = r.replace('Please Choose Model', '')
    
    text = texts.replace('Please Select Aspect Ratio', '')
    if to_real:
        
        user_from = f"{callback_query.from_user.id}"
        is_user = user_from in user
        if not is_user:
            await callback_query.answer("You Are Not Auth")
        if is_user:
            
            try:
                size = 512
                sizes = 512
                keyboard = [[
                    InlineKeyboardButton("Anime Journey",
                                         callback_data=f"animejourney_{user}_{size}_{sizes}"),
                    InlineKeyboardButton("Anything V3",
                                         callback_data=f"anythingv3_{user}_{size}_{sizes}"),
                                  
                    InlineKeyboardButton("Midjourney",
                                         callback_data=f"midjourney_{user}_{size}_{sizes}"),
                ],
                [
                    InlineKeyboardButton("Deliberate",
                                         callback_data=f"deliberate_{user}_{size}_{sizes}"),
                    InlineKeyboardButton("Dosmix",
                                         callback_data=f"dosmix_{user}_{size}_{sizes}"),
                                  
                    InlineKeyboardButton("Chilloutmix",
                                         callback_data=f"chilloutmix_{user}_{size}_{sizes}"),
                ],
                [
                    InlineKeyboardButton("DreamShaper",
                                         callback_data=f"dreamshaper_{user}_{size}_{sizes}"),
                    InlineKeyboardButton("Counterfeit",
                                         callback_data=f"counterfeit_{userid}_{size}_{sizes}"),
                                  
                    InlineKeyboardButton("MeinaMix",
                                         callback_data=f"meinamix_{userid}_{size}_{sizes}"),
                                         
                ]]
                reply_markup = InlineKeyboardMarkup(keyboard)
                await callback_query.message.edit_text(  
                     text=f"{text}\n Please Choose Model",
                     reply_markup=reply_markup)

                
            except Exception as e:
                print(e)
                await app.send_message(
                    chatid,
                    text=f"⚠️ Please Try Again")
                
    if to_model:
        
        user_from = f"{callback_query.from_user.id}"
        is_user = user_from in user
        if not is_user:
            await callback_query.answer("You Are Not Auth")
        if is_user:
            
            try:
                size = 768
                sizes = 512
                keyboard = [[
                    InlineKeyboardButton("Anime Journey",
                                         callback_data=f"animejourney_{user}_{size}_{sizes}"),
                    InlineKeyboardButton("Anything V3",
                                         callback_data=f"anythingv3_{user}_{size}_{sizes}"),
                                  
                    InlineKeyboardButton("Midjourney",
                                         callback_data=f"midjourney_{user}_{size}_{sizes}"),
                ],
                [
                    InlineKeyboardButton("Deliberate",
                                         callback_data=f"deliberate_{user}_{size}_{sizes}"),
                    InlineKeyboardButton("Dosmix",
                                         callback_data=f"dosmix_{user}_{size}_{sizes}"),
                                  
                    InlineKeyboardButton("Chilloutmix",
                                         callback_data=f"chilloutmix_{user}_{size}_{sizes}"),
                ],
                [
                    InlineKeyboardButton("DreamShaper",
                                         callback_data=f"dreamshaper_{user}_{size}_{sizes}"),
                    InlineKeyboardButton("Counterfeit",
                                         callback_data=f"counterfeit_{userid}_{size}_{sizes}"),
                                  
                    InlineKeyboardButton("MeinaMix",
                                         callback_data=f"meinamix_{userid}_{size}_{sizes}"),
                                         
                ]]
                reply_markup = InlineKeyboardMarkup(keyboard)
                await callback_query.message.edit_text(
                     text=f"{text}\n Please Choose Model",
                     reply_markup=reply_markup)

                
            except Exception as e:
                print(e)
                await app.send_message(
                    chatid,
                    text=f"⚠️ Please Try Again")
               
    if to_reals:
        
        user_from = f"{callback_query.from_user.id}"
        is_user = user_from in user
        if not is_user:
            await callback_query.answer("You Are Not Auth")
        if is_user:
            
            try:
                size = 512
                sizes = 768
                keyboard = [[
                    InlineKeyboardButton("Anime Journey",
                                         callback_data=f"animejourney_{user}_{size}_{sizes}"),
                    InlineKeyboardButton("Anything V3",
                                         callback_data=f"anythingv3_{user}_{size}_{sizes}"),
                                  
                    InlineKeyboardButton("Midjourney",
                                         callback_data=f"midjourney_{user}_{size}_{sizes}"),
                ],
                [
                    InlineKeyboardButton("Deliberate",
                                         callback_data=f"deliberate_{user}_{size}_{sizes}"),
                    InlineKeyboardButton("Dosmix",
                                         callback_data=f"dosmix_{user}_{size}_{sizes}"),
                                  
                    InlineKeyboardButton("Chilloutmix",
                                         callback_data=f"chilloutmix_{user}_{size}_{sizes}"),
                ],
                [
                    InlineKeyboardButton("DreamShaper",
                                         callback_data=f"dreamshaper_{user}_{size}_{sizes}"),
                    InlineKeyboardButton("Counterfeit",
                                         callback_data=f"counterfeit_{userid}_{size}_{sizes}"),
                                  
                    InlineKeyboardButton("MeinaMix",
                                         callback_data=f"meinamix_{userid}_{size}_{sizes}"),
                                         
                ]]
                reply_markup = InlineKeyboardMarkup(keyboard)
                await callback_query.message.edit_text(
                     text=f"{text}\n Please Choose Model",
                     reply_markup=reply_markup)

                
            except Exception as e:
                print(e)
                await app.send_message(
                    chatid,
                    text=f"⚠️ Please Try Again")
    if to_animejourney:
        
        user_from = f"{callback_query.from_user.id}"
        is_user = user_from in user
        if not is_user:
            await callback_query.answer("You Are Not Auth")
        if is_user:
            K = await callback_query.message.edit_text(text="Please Wait Few Minutes")
            id = "anime-journey"
            width = Kn[2]
            height = Kn[3]

            

           



          
            
            data = {
                "key": key,
                "model_id": id,
                "prompt": text,
                "negative_prompt": "nsfw",
                "width": width,
                "height": height,
                "samples": "1",
                "num_inference_steps": "30",
                "safety_checker": "no",
                "enhance_prompt": "no",
                "seed": None,
                "guidance_scale": 7.5,
                "webhook": None,
                "track_id": None
            }
            response = requests.post("https://stablediffusionapi.com/api/v3/dreambooth", json=data)
            resp = response.json()
            try:
                await app.send_photo(
                    chatid,
                    photo=f"{resp['output'][0]}",
                    caption=
                    f"Prompt - **{text}**\n**[{callback_query.from_user.first_name}-Kun](tg://user?id={callback_query.from_user.id})**\nModel - AnimeJourney"
                )

                
            except:
                fetch = resp['fetch_result']
                await asyncio.sleep(30)
                result = requests.post(fetch, data=json.dumps({'key': key}), headers={'Content-Type': 'application/json'})
                resultk = result.json()    
                try:
                    await app.send_photo(
                        chatid,
                        photo=f"{resultk['output'][0]}",
                        caption=
                        f"Prompt - **{text}**\n**[{callback_query.from_user.first_name}-Kun](tg://user?id={callback_query.from_user.id})**\nModel - AnimeJourney"
                    )

                
                except:
                    fetch = resp['fetch_result']
                    await asyncio.sleep(100)
                    result = requests.post(fetch, data=json.dumps({'key': key}), headers={'Content-Type': 'application/json'})
                    resultk = result.json()
                    await app.send_photo(
                        chatid,
                        photo=f"{resultk['output'][0]}",
                        caption=
                        f"Prompt - **{text}**\n**[{callback_query.from_user.first_name}-Kun](tg://user?id={callback_query.from_user.id})**\nModel - AnimeJourney"
                    )

              
    if to_midjourney:
        
        user_from = f"{callback_query.from_user.id}"
        is_user = user_from in user
        if not is_user:
            await callback_query.answer("You Are Not Auth")
        if is_user:
            K = await callback_query.message.edit_text(text="Please Wait Few Minutes")
            id = "midjourney"
            aspect_ratio = Kn[2]

            

           



            width = Kn[2]
            height = Kn[3]
            data = {
                "key": key,
                "model_id": id,
                "prompt": text,
                "negative_prompt": "nsfw",
                "width": width,
                "height": height,
                "samples": "1",
                "num_inference_steps": "30",
                "safety_checker": "no",
                "enhance_prompt": "no",
                "seed": None,
                "guidance_scale": 7.5,
                "webhook": None,
                "track_id": None
            }
            print(text)
            response = requests.post("https://stablediffusionapi.com/api/v3/dreambooth", json=data)
            resp = response.json()
            print(resp)
            try:
                await app.send_photo(
                    chatid,
                    photo=f"{resp['output'][0]}",
                    caption=
                    f"Prompt - **{text}**\n**[{callback_query.from_user.first_name}-Kun](tg://user?id={callback_query.from_user.id})**\nModel - Midjourney"
                )

              
            except:
                fetch = resp['fetch_result']
                await asyncio.sleep(30)
                result = requests.post(fetch, data=json.dumps({'key': key}), headers={'Content-Type': 'application/json'})
                resultk = result.json()    
                try:
                    await app.send_photo(
                        chatid,
                        photo=f"{resultk['output'][0]}",
                        caption=
                        f"Prompt - **{text}**\n**[{callback_query.from_user.first_name}-Kun](tg://user?id={callback_query.from_user.id})**\nModel - Midjourney"
                    )

                  
                except:
                    fetch = resp['fetch_result']
                    await asyncio.sleep(100)
                    result = requests.post(fetch, data=json.dumps({'key': key}), headers={'Content-Type': 'application/json'})
                    resultk = result.json()
                    await app.send_photo(
                        chatid,
                        photo=f"{resultk['output'][0]}",
                        caption=
                        f"Prompt - **{text}**\n**[{callback_query.from_user.first_name}-Kun](tg://user?id={callback_query.from_user.id})**\nModel - Midjourney"
                    )

                  
    if to_anything:
        
        user_from = f"{callback_query.from_user.id}"
        is_user = user_from in user
        if not is_user:
            await callback_query.answer("You Are Not Auth")
        if is_user:
            K = await callback_query.message.edit_text(text="Please Wait Few Minutes")
            id = "anything-v3"
            aspect_ratio = Kn[2]

            

           



            width = Kn[2]
            height = Kn[3]
            data = {
                "key": key,
                "model_id": id,
                "prompt": text,
                "negative_prompt": "nsfw",
                "width": width,
                "height": height,
                "samples": "1",
                "num_inference_steps": "30",
                "safety_checker": "no",
                "enhance_prompt": "no",
                "seed": None,
                "guidance_scale": 7.5,
                "webhook": None,
                "track_id": None
            }
            response = requests.post("https://stablediffusionapi.com/api/v3/dreambooth", json=data)
            resp = response.json()
            try:
                await app.send_photo(
                    chatid,
                    photo=f"{resp['output'][0]}",
                    caption=
                    f"Prompt - **{text}**\n**[{callback_query.from_user.first_name}-Kun](tg://user?id={callback_query.from_user.id})**\nModel - Anything V3"
                )

               
            except:
                fetch = resp['fetch_result']
                await asyncio.sleep(30)
                result = requests.post(fetch, data=json.dumps({'key': key}), headers={'Content-Type': 'application/json'})
                resultk = result.json()    
                try:
                    await app.send_photo(
                        chatid,
                        photo=f"{resultk['output'][0]}",
                        caption=
                        f"Prompt - **{text}**\n**[{callback_query.from_user.first_name}-Kun](tg://user?id={callback_query.from_user.id})**\nModel - Anything v3"
                    )

                    
                except:
                    fetch = resp['fetch_result']
                    await asyncio.sleep(100)
                    result = requests.post(fetch, data=json.dumps({'key': key}), headers={'Content-Type': 'application/json'})
                    resultk = result.json()
                    await app.send_photo(
                        chatid,
                        photo=f"{resultk['output'][0]}",
                        caption=
                        f"Prompt - **{text}**\n**[{callback_query.from_user.first_name}-Kun](tg://user?id={callback_query.from_user.id})**\nModel - Anything V3"
                    )

                    
    if to_deliberate:
        
        user_from = f"{callback_query.from_user.id}"
        is_user = user_from in user
        if not is_user:
            await callback_query.answer("You Are Not Auth")
        if is_user:
            K = await callback_query.message.edit_text(text="Please Wait Few Minutes")
            id = "deliberate-v2"
            aspect_ratio = Kn[2]

            

           



            width = Kn[2]
            height = Kn[3]
            data = {
                "key": key,
                "model_id": id,
                "prompt": text,
                "negative_prompt": "nsfw",
                "width": width,
                "height": height,
                "samples": "1",
                "num_inference_steps": "30",
                "safety_checker": "no",
                "enhance_prompt": "no",
                "seed": None,
                "guidance_scale": 7.5,
                "webhook": None,
                "track_id": None
            }
            response = requests.post("https://stablediffusionapi.com/api/v3/dreambooth", json=data)
            resp = response.json()
            try:
                await app.send_photo(
                    chatid,
                    photo=f"{resp['output'][0]}",
                    caption=
                    f"Prompt - **{text}**\n**[{callback_query.from_user.first_name}-Kun](tg://user?id={callback_query.from_user.id})**\nModel - Deliberate"
                )

                
            except:
                fetch = resp['fetch_result']
                await asyncio.sleep(30)
                result = requests.post(fetch, data=json.dumps({'key': key}), headers={'Content-Type': 'application/json'})
                resultk = result.json()    
                try:
                    await app.send_photo(
                        chatid,
                        photo=f"{resultk['output'][0]}",
                        caption=
                        f"Prompt - **{text}**\n**[{callback_query.from_user.first_name}-Kun](tg://user?id={callback_query.from_user.id})**\nModel - Deliberate"
                    )

                    
                except:
                    fetch = resp['fetch_result']
                    await asyncio.sleep(100)
                    result = requests.post(fetch, data=json.dumps({'key': key}), headers={'Content-Type': 'application/json'})
                    resultk = result.json()
                    await app.send_photo(
                        chatid,
                        photo=f"{resultk['output'][0]}",
                        caption=
                        f"Prompt - **{text}**\n**[{callback_query.from_user.first_name}-Kun](tg://user?id={callback_query.from_user.id})**\nModel - Deliberate"
                    )

                  
    if to_dosmix:
        
        user_from = f"{callback_query.from_user.id}"
        is_user = user_from in user
        if not is_user:
            await callback_query.answer("You Are Not Auth")
        if is_user:
            K = await callback_query.message.edit_text(text="Please Wait Few Minutes")
            id = "dosmix"
            aspect_ratio = Kn[2]

            

           



            width = Kn[2]
            height = Kn[3]
            data = {
                "key": key,
                "model_id": id,
                "prompt": text,
                "negative_prompt": "nsfw",
                "width": width,
                "height": height,
                "samples": "1",
                "num_inference_steps": "30",
                "safety_checker": "no",
                "enhance_prompt": "no",
                "seed": None,
                "guidance_scale": 7.5,
                "webhook": None,
                "track_id": None
            }
            response = requests.post("https://stablediffusionapi.com/api/v3/dreambooth", json=data)
            resp = response.json()
            try:
                await app.send_photo(
                    chatid,
                    photo=f"{resp['output'][0]}",
                    caption=
                    f"Prompt - **{text}**\n**[{callback_query.from_user.first_name}-Kun](tg://user?id={callback_query.from_user.id})**\nModel - Dosmix"
                )

               
            except:
                fetch = resp['fetch_result']
                await asyncio.sleep(30)
                result = requests.post(fetch, data=json.dumps({'key': key}), headers={'Content-Type': 'application/json'})
                resultk = result.json()    
                try:
                    await app.send_photo(
                        chatid,
                        photo=f"{resultk['output'][0]}",
                        caption=
                        f"Prompt - **{text}**\n**[{callback_query.from_user.first_name}-Kun](tg://user?id={callback_query.from_user.id})**\nModel - Dosmix"
                    )

                    
                except:
                    fetch = resp['fetch_result']
                    await asyncio.sleep(100)
                    result = requests.post(fetch, data=json.dumps({'key': key}), headers={'Content-Type': 'application/json'})
                    resultk = result.json()
                    await app.send_photo(
                        chatid,
                        photo=f"{resultk['output'][0]}",
                        caption=
                        f"Prompt - **{text}**\n**[{callback_query.from_user.first_name}-Kun](tg://user?id={callback_query.from_user.id})**\nModel - Dosmix"
                    )

                   
    if to_meinamix:
        
        user_from = f"{callback_query.from_user.id}"
        is_user = user_from in user
        if not is_user:
            await callback_query.answer("You Are Not Auth")
        if is_user:
            K = await callback_query.message.edit_text(text="Please Wait Few Minutes")
            id = "meinamix"
            aspect_ratio = Kn[2]

            

           



            width = Kn[2]
            height = Kn[3]
            data = {
                "key": key,
                "model_id": id,
                "prompt": text,
                "negative_prompt": "nsfw",
                "width": width,
                "height": height,
                "samples": "1",
                "num_inference_steps": "30",
                "safety_checker": "no",
                "enhance_prompt": "no",
                "seed": None,
                "guidance_scale": 7.5,
                "webhook": None,
                "track_id": None
            }
            response = requests.post("https://stablediffusionapi.com/api/v3/dreambooth", json=data)
            resp = response.json()
            try:
                await app.send_photo(
                    chatid,
                    photo=f"{resp['output'][0]}",
                    caption=
                    f"Prompt - **{text}**\n**[{callback_query.from_user.first_name}-Kun](tg://user?id={callback_query.from_user.id})**\nModel - MeinaMix"
                )

            except:
                fetch = resp['fetch_result']
                await asyncio.sleep(30)
                result = requests.post(fetch, data=json.dumps({'key': key}), headers={'Content-Type': 'application/json'})
                resultk = result.json()    
                try:
                    await app.send_photo(
                        chatid,
                        photo=f"{resultk['output'][0]}",
                        caption=
                        f"Prompt - **{text}**\n**[{callback_query.from_user.first_name}-Kun](tg://user?id={callback_query.from_user.id})**\nModel - MeinaMix"
                    )

                except:
                    fetch = resp['fetch_result']
                    await asyncio.sleep(100)
                    result = requests.post(fetch, data=json.dumps({'key': key}), headers={'Content-Type': 'application/json'})
                    resultk = result.json()
                    await app.send_photo(
                        chatid,
                        photo=f"{resultk['output'][0]}",
                        caption=
                        f"Prompt - **{text}**\n**[{callback_query.from_user.first_name}-Kun](tg://user?id={callback_query.from_user.id})**\nModel - MeinaMix"
                    )

                  
                    
    if to_chilloutmix:
        
        user_from = f"{callback_query.from_user.id}"
        is_user = user_from in user
        if not is_user:
            await callback_query.answer("You Are Not Auth")
        if is_user:
            K = await callback_query.message.edit_text(text="Please Wait Few Minutes")
            id = "chilloutmix"
            aspect_ratio = Kn[2]

            

           



            width = Kn[2]
            height = Kn[3]
            data = {
                "key": key,
                "model_id": id,
                "prompt": text,
                "negative_prompt": "nsfw",
                "width": width,
                "height": height,
                "samples": "1",
                "num_inference_steps": "30",
                "safety_checker": "no",
                "enhance_prompt": "no",
                "seed": None,
                "guidance_scale": 7.5,
                "webhook": None,
                "track_id": None
            }
            response = requests.post("https://stablediffusionapi.com/api/v3/dreambooth", json=data)
            resp = response.json()
            try:
                await app.send_photo(
                    chatid,
                    photo=f"{resp['output'][0]}",
                    caption=
                    f"Prompt - **{text}**\n**[{callback_query.from_user.first_name}-Kun](tg://user?id={callback_query.from_user.id})**\nModel - Chilloutmix"
                )

            
            except:
                fetch = resp['fetch_result']
                await asyncio.sleep(30)
                result = requests.post(fetch, data=json.dumps({'key': key}), headers={'Content-Type': 'application/json'})
                resultk = result.json()    
                try:
                    await app.send_photo(
                        chatid,
                        photo=f"{resultk['output'][0]}",
                        caption=
                        f"Prompt - **{text}**\n**[{callback_query.from_user.first_name}-Kun](tg://user?id={callback_query.from_user.id})**\nModel - Chilloutmix"
                    )

                  
                except:
                    fetch = resp['fetch_result']
                    await asyncio.sleep(100)
                    result = requests.post(fetch, data=json.dumps({'key': key}), headers={'Content-Type': 'application/json'})
                    resultk = result.json()
                    await app.send_photo(
                        chatid,
                        photo=f"{resultk['output'][0]}",
                        caption=
                        f"Prompt - **{text}**\n**[{callback_query.from_user.first_name}-Kun](tg://user?id={callback_query.from_user.id})**\nModel - Chilloutmix"
                    )

                    
    if to_dreamshaper:
        
        user_from = f"{callback_query.from_user.id}"
        is_user = user_from in user
        if not is_user:
            await callback_query.answer("You Are Not Auth")
        if is_user:
            K = await callback_query.message.edit_text(text="Please Wait Few Minutes")
            id = "dream-shaper-8797"
            aspect_ratio = Kn[2]
            if aspect_ratio == "square":
                width = 512
                height = 512
            if aspect_ratio == "portrait":
                width = 512
                height = 768
            if aspect_ratio == "landscape":
                width = 768
                height = 512
            
            data = {
                "key": key,
                "model_id": id,
                "prompt": text,
                "negative_prompt": "nsfw",
                "width": width,
                "height": height,
                "samples": "1",
                "num_inference_steps": "30",
                "safety_checker": "no",
                "enhance_prompt": "no",
                "seed": None,
                "guidance_scale": 7.5,
                "webhook": None,
                "track_id": None
            }
            response = requests.post("https://stablediffusionapi.com/api/v3/dreambooth", json=data)
            resp = response.json()
            try:
                await app.send_photo(
                    chatid,
                    photo=f"{resp['output'][0]}",
                    caption=
                    f"Prompt - **{text}**\n**[{callback_query.from_user.first_name}-Kun](tg://user?id={callback_query.from_user.id})**\nModel - Dreamshaper"
                )

                
            except:
                fetch = resp['fetch_result']
                await asyncio.sleep(30)
                result = requests.post(fetch, data=json.dumps({'key': key}), headers={'Content-Type': 'application/json'})
                resultk = result.json()    
                try:
                    await app.send_photo(
                        chatid,
                        photo=f"{resultk['output'][0]}",
                        caption=
                        f"Prompt - **{text}**\n**[{callback_query.from_user.first_name}-Kun](tg://user?id={callback_query.from_user.id})**\nModel - Dreamshaper"
                    )

                except:
                    fetch = resp['fetch_result']
                    await asyncio.sleep(100)
                    result = requests.post(fetch, data=json.dumps({'key': key}), headers={'Content-Type': 'application/json'})
                    resultk = result.json()
                    await app.send_photo(
                        chatid,
                        photo=f"{resultk['output'][0]}",
                        caption=
                        f"Prompt - **{text}**\n**[{callback_query.from_user.first_name}-Kun](tg://user?id={callback_query.from_user.id})**\nModel - Dreamshaper"
                    )

                    
    if to_counterfeit:
        
        user_from = f"{callback_query.from_user.id}"
        is_user = user_from in user
        if not is_user:
            await callback_query.answer("You Are Not Auth")
        if is_user:
            K = await callback_query.message.edit_text(text="Please Wait Few Minutes")
            id = "counterfeit-v25"
            aspect_ratio = Kn[2]

            

           



            width = Kn[2]
            height = Kn[3]
            data = {
                "key": key,
                "model_id": id,
                "prompt": text,
                "negative_prompt": "nsfw",
                "width": width,
                "height": height,
                "samples": "1",
                "num_inference_steps": "30",
                "safety_checker": "no",
                "enhance_prompt": "no",
                "seed": None,
                "guidance_scale": 7.5,
                "webhook": None,
                "track_id": None
            }
            response = requests.post("https://stablediffusionapi.com/api/v3/dreambooth", json=data)
            resp = response.json()
            try:
                await app.send_photo(
                    chatid,
                    photo=f"{resp['output'][0]}",
                    caption=
                    f"Prompt - **{text}**\n**[{callback_query.from_user.first_name}-Kun](tg://user?id={callback_query.from_user.id})**\nModel - Counterfeit"
                )

                
            except:
                fetch = resp['fetch_result']
                await asyncio.sleep(30)
                result = requests.post(fetch, data=json.dumps({'key': key}), headers={'Content-Type': 'application/json'})
                resultk = result.json()    
                try:
                    await app.send_photo(
                        chatid,
                        photo=f"{resultk['output'][0]}",
                        caption=
                        f"Prompt - **{text}**\n**[{callback_query.from_user.first_name}-Kun](tg://user?id={callback_query.from_user.id})**\nModel - Counterfeit"
                    )

                   
                except:
                    fetch = resp['fetch_result']
                    await asyncio.sleep(100)
                    result = requests.post(fetch, data=json.dumps({'key': key}), headers={'Content-Type': 'application/json'})
                    resultk = result.json()
                    await app.send_photo(
                        chatid,
                        photo=f"{resultk['output'][0]}",
                        caption=
                        f"Prompt - **{text}**\n**[{callback_query.from_user.first_name}-Kun](tg://user?id={callback_query.from_user.id})**\nModel - Counterfeit"
                    )

                    
         
                    
   
         
                    
   
         
                  

@app.on_message(filters.command(["draw"]))
async def mangadown(client, message):
    msgs = message.text.split(' ', 1)
    if len(msgs) == 1:
        await message.reply_text("Format : /draw < text to anime image >")
        return
    kmsg = msgs[1]
    search = kmsg if True else ' '.join([kmsg])
    for word in words:
        for word2 in search.translate(str.maketrans('', '', string.punctuation)).split():
            if word.lower() == word2.lower():              
                await message.reply_text(f"You tried to use a nsfw blacklist word! ({word})")
                return
    user = message.from_user.id
    

        
        msg = msgs[1]
        userid = message.from_user.id

        keyboard = [[
            InlineKeyboardButton("Square",
                                 callback_data=f"square_{userid}"),
            InlineKeyboardButton("Landscape",
                                 callback_data=f"landscape_{userid}"),
                                 
            InlineKeyboardButton("Portrait",
                                 callback_data=f"portrait_{userid}"),
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await message.reply_text(
            text=f"{msg}\n Please Select Aspect Ratio",
            reply_markup=reply_markup,
            quote=False,
        )
        
    



@app.on_message(filters.command(["start"], prefixes=["/", "!"]))
async def start(client, message):
          
    ]]
    keyboard = [[
        InlineKeyboardButton("Support", url="https://discord.gg/v7AW8nD8dD"),
    ],
                [
                    InlineKeyboardButton(
                        "Add to your group",
                        url=f"http://t.me/waifuairobot?startgroup=true")
                ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await message.reply_text(
        text=
        f"Hello! I'm Stablediffusionapi.com",
        reply_markup=reply_markup)
    


app.run()

