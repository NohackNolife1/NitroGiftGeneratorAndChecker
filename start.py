import random, string, webbrowser, time, requests, os, asyncio, json, traceback, re, httpx, platform
from random import randint
from os import system
from discord.ext import commands
from colorama import Fore, init

print("""
███╗░░██╗██╗████████╗██████╗░░█████╗░░░░░░░░██████╗░██╗███████╗████████╗
████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗░░░░░░██╔════╝░██║██╔════╝╚══██╔══╝
██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║█████╗██║░░██╗░██║█████╗░░░░░██║░░░
██║╚████║██║░░░██║░░░██╔══██╗██║░░██║╚════╝██║░░╚██╗██║██╔══╝░░░░░██║░░░
██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝░░░░░░╚██████╔╝██║██║░░░░░░░░██║░░░
╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░░░░░░░╚═════╝░╚═╝╚═╝░░░░░░░░╚═╝░░░

░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝

░░░░░░░░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
░░██╗░░██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██████╗██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
╚═██╔═╝██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
░░╚═╝░░╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
░░░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝""")
time.sleep(2)
print("Creator  -  Zafros ")
time.sleep(0.3)
print("https://github.com/Zafros56   \n")
#Add
print("Remixed by NohackNolife1")
time.sleep(0.2)


def NoToken
     for n in range(int(num)):
       f=open("Nitro Codes.txt","w", encoding='utf-8')
       print("Wait, Generating for you!")
       y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(24))
       f.write('https://discord.gift/')
       f.write(y)
       f.write("\n")
       f.close()
#Checker Here
     with open("Nitro Codes.txt") as f:
         for line in f:
            nitro = line.strip("\n")
             url = "https://discordapp.com/api/v9/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"
             r = requests.get(url)
             if r.status_code == 200:
                 print(" Valid | {} ".format(line.strip("\n")))
                 os._exit(1)
             if r.status_code == 429:
                 print(" RateLimited, Not Checked. Waiting a 15min | {} ".format(line.strip("\n")))
                 time.sleep(900)
                 print("Ok, Start Checker.")
             else:
        	     print(" Invalid | {} ".format(line.strip("\n")))
            
def UseToken
     for n in range(int(num)):
       f=open("Nitro Codes.txt","w", encoding='utf-8')
       print("Wait, Generating for you!")
       y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(24))
       f.write('https://discord.gift/')
       f.write(y)
       f.write("\n")
       f.close()
     with open("Nitro Codes.txt") as f:
         for line in f:
            nitro = line.strip("\n")
#ねむねむなので別の人のCode
#参考元 https://github.com/Vedza/NitroSniper
async with httpx.AsyncClient() as client:
    result = await client.post(
        'https://discordapp.com/api/v9/entitlements/gift-codes/' + nitro + '/redeem',
        headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
     try:
         print(
             Fore.LIGHTGREEN_EX + "[-] Scanned code: " + Fore.LIGHTRED_EX + nitro + Fore.RESET)
                    if 'This gift has been redeemed already' in str(result.content):
                        print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
                        print(Fore.LIGHTYELLOW_EX + "[-] Code has been already redeemed" + Fore.RESET,
                              end='')
                    elif 'nitro' in str(result.content):
                        print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
                        print(Fore.GREEN + "[+] Code applied" + Fore.RESET, end='')
                    elif 'Unknown Gift Code' in str(result.content):
                        print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
                        print(Fore.LIGHTRED_EX + "[-] Invalid Code" + Fore.RESET, end=' ')
                    print(" Delay:" + Fore.GREEN + " %.3fs" % delay + Fore.RESET)
            
num=input('Input How Many Codes to Generate and Check: ')
#add
qt = input("Auto Active Nitro? y/n (Default n)")
if qt == "y"
    Token = input("Input Token Here.\n->")
    UseToken()
elif qt == "Y"
    Token = input("Input Token Here.\n->")
    UseToken()
elif qt == "n"
    NoToken()
elif qt == ""
    print("No Input, NoTokenMode.")
    NoToken()
else: 
    print("Wrong Input, NoTokenMode.") 
    NoToken()
# これ見てる人へ。
# 彼氏ほしくなりました。
# あまーいあまーい、そんな恋をしてみたくなりました。
# 私なんかのGithubを見る人も少なくて、Codeを見る人も少ないでしょうが。
# それでも希望を持ちたい生物なので。
# なんか恐らく100%連絡取れそうなTwitter書きます。
# @PmoMl1
# 連絡取れても私は声も出さないでしょうし、顔も、リアルのことも一切話さないとは思いますけど、それでもチャットだけでのやり取り又は私が完全聞き専でも良いって方は連絡ください。
# まぁ多分こんなの一時的な突発的感情なんでしょうがw
# 後変なのは無視します。
# 2日間以上来なかったら無視か冬眠してます。
