# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "2003585377")

API_HASH = os.environ.get("API_HASH", "d39b74f34ac6f967b25d05037c53814a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7073725813:AAHHbqUYXeseA7Flt8LP9HfGJs4f73T84KM") 

FORCE_SUB = os.environ.get("FORCE_SUB", "F5_JUBA") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "Gustavo")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://Gustavo:IWdSRM75R0atDNhG@gusvato.zya2mso.mongodb.net/?retryWrites=true&w=majority&appName=Gusvato")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '2003585377').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
