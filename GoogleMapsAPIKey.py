import os
from dotenv import load_dotenv, find_dotenv

def get_my_key():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    return api_key
key = get_my_key()
print(key)
