## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQAt_qgh6CS8nHIo7k-B7g2YBcvfUQiL3o9klfqmzlkhmL_uWP-WuhpgGsE9XOySpSF6DXbyrmO4g9XUjTcAmHc3vQVuMbVvje9cGdjUInsrsHUPJjpsJMIu--VMoxuUaWHsyr_5evuV-MtsjegtgtdqB0okgct2LwqwxrarHqSR1_GYhe88pB8Q15_-u9xTBfEm2C0DIuSCCE6Zsn8XEwio9Zpw0S8SqgbQDPpVHRNYatwqhGFyGqOGSPJqlbqb4CSvxfNm94CCNFySPvI2C1udqtKlzuC_lzHbW-6vWqIr599vgJiXPCiqATzSY4hc5SpFBaDLuIqS5PV6cjdxCxUXAAAAATLLfbUA")
BOT_TOKEN = getenv("BOT_TOKEN", "5291027175:AAHZOapGkUgARhfaOhYXCxb4rZQ89I7ER6s")
BOT_NAME = getenv("BOT_NAME", "AHFFRTbot")
API_ID = int(getenv("API_ID", "13814219"))
API_HASH = getenv("API_HASH", "63c10cdc0f579b9e95d4ebfa9484b8cd")
OWNER_NAME = getenv("OWNER_NAME", "Mazen")
OWNER_USERNAME = getenv("OWNER_USERNAME", "SSaLi")
ALIVE_NAME = getenv("ALIVE_NAME", "sally")
BOT_USERNAME = getenv("BOT_USERNAME", "TSSERU3bot")
OWNER_ID = getenv("OWNER_ID", "5306882974")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "IRIIRll")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Dl777l")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TlTT5")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5306882974").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
