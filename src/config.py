import os
from dotenv import load_dotenv

load_dotenv(override=True)

config: dict = {
    "DISCORD_TOKEN": os.environ["DISCORD_TOKEN"],
}