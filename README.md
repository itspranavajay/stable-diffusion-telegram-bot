# AI Powered Art in a Telegram Bot!

## Setup

Install requirements

`pip install -r requirements.txt`

My Bot uses [Automatic1111's WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) as the backend.
Follow the directions on their repo for setup instructions.

Once you have WebUI set up, run `webui.sh` with the `--api` argument. You can also add other
arguments such as `--xformers` to use xformers memory efficient attention.

You can use the web ui interface that Automatic1111 provides to select the model and VAE to use.
Their repo has documentation on how to do so. I also recommend doing a test generation

Create a file called `.env` in the same folder as `main.py`. Inside the `.env` file,
create a line `TOKEN = xxxx`, where xxxx is your telegram bot token.
create a line `API_ID = xxxx`, where xxxx is your telegram id api id.
create a line `API_HASH = xxxx`, where xxxx is your telegram id api hash.
create a line `SD_URL = xxxx`, where xxxx is your sd api url.

Now, you can run the bot

`python main.py`

### Any questions or need help? Come hop on by to our Telegram Group!

[Otakatsu Chat](https://t.me/otakatsu_chat)


