from pypresence import Presence
import threading 
import os 
import random 
import requests 
from pystyle import Colors, Colorate 
import time 
import ctypes

def TitoloDaGaming(title):
    TitleBytez = title.encode('cp1252')
    ctypes.windll.kernel32.SetConsoleTitleA(TitleBytez)

def ConfigurationRPC():
    RPC = Presence(client_id="1169401122469986388")
    RPC.connect()
    RPC.update(
        state="Violet Spammer",
        details="Advanced NGL Spammer",
        large_image="uwuspam",
        large_text="I love Threads"
    )
    return RPC

TitoloDaGaming("Violet Spammer")

# Delete Exploit 

def ReqWithThings(username):
    games = ['', 'confessions', '3words', 'wfriendship', 'rizzme', 'tbh', 'shipme', 'yourcrush', 'cancelled', 'dealbreaker']
    gameslugg = random.choice(games)

    def genrandomidd(): 
        return ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for _ in range(30)) 

    def randomname(): 
        return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(8)) 

    url = "https://ngl.link/api/submit"

    headers = {
    
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "ngl.link",
        "Origin": "https://ngl.link",
    }

    question = 'function(deleter):____reset(fuck_you_)'
    randomdeviceid = genrandomidd()
    randomgeneratedusername = randomname()

    

    data = {

        "username": username,
        "question": question,
        "deviceId": randomdeviceid,
        "gameSlug": gameslugg
    }

    response = requests.post(url, data=data, headers=headers)

    return username, randomgeneratedusername

def sendspam():

    R = '\033[31m'
    G = '\033[32m'
    W = '\033[0m'
    P = '\033[38;5;92m'
    os.system('cls' if os.name == 'nt' else 'clear')

    print(Colorate.Diagonal(Colors.blue_to_purple,"""
 ██▒   █▓ ██▓ ▒█████   ██▓    ▓█████▄▄▄█████▓ 
▓██░   █▒▓██▒▒██▒  ██▒▓██▒    ▓█   ▀▓  ██▒ ▓▒ 
 ▓██  █▒░▒██▒▒██░  ██▒▒██░    ▒███  ▒ ▓██░ ▒░ 
  ▒██ █░░░██░▒██   ██░▒██░    ▒▓█  ▄░ ▓██▓ ░  
   ▒▀█░  ░██░░ ████▓▒░░██████▒░▒████▒ ▒██▒ ░   
   ░ ▐░  ░▓  ░ ▒░▒░▒░ ░ ▒░▓  ░░░ ▒░ ░ ▒ ░░    
                Hisako Domina        
    """))
    
    input_username = input(Colorate.Diagonal(Colors.blue_to_purple, "Username: "))
    num_threads = int(input(Colorate.Vertical(Colors.blue_to_purple,"Number of threads:"))) 
    print("")
    while True:
        username, random_username = ReqWithThings(input_username)
        print(G+"  [✔]"+W+f"Inbox deleter exploit sent to {username}")
        
    threads = [] 
    for i in range(num_threads): 
        t = threading.Thread(target=ReqWithThings) 
        threads.append(t) 
        t.start() 

    for t in threads: 
        t.join()         

# Custom Spam By User

def CustomSpam(): 
    R = '\033[31m' 
    G = '\033[32m' 
    W = '\033[0m' 

    os.system('cls' if os.name == 'nt' else 'clear') 

    print(Colorate.Vertical(Colors.blue_to_purple,""" 
 ██▒   █▓ ██▓ ▒█████   ██▓    ▓█████▄▄▄█████▓ 
▓██░   █▒▓██▒▒██▒  ██▒▓██▒    ▓█   ▀▓  ██▒ ▓▒ 
 ▓██  █▒░▒██▒▒██░  ██▒▒██░    ▒███  ▒ ▓██░ ▒░ 
  ▒██ █░░░██░▒██   ██░▒██░    ▒▓█  ▄░ ▓██▓ ░  
   ▒▀█░  ░██░░ ████▓▒░░██████▒░▒████▒ ▒██▒ ░   
   ░ ▐░  ░▓  ░ ▒░▒░▒░ ░ ▒░▓  ░░░ ▒░ ░ ▒ ░░    
                Hisako Domina        
    """)) 

    nglusername = input(Colorate.Vertical(Colors.blue_to_purple,"Username: ")) 
    message = input(Colorate.Vertical(Colors.blue_to_purple,"Message: ")) 
    Count = int(input(Colorate.Vertical(Colors.blue_to_purple,"Count:"))) 
    num_threads = int(input(Colorate.Vertical(Colors.blue_to_purple,"Number of threads:"))) 
    use_proxy = input(Colorate.Vertical(Colors.blue_to_purple,"Use proxy? (y/n): ")) 

    if use_proxy.lower() == 'y':
        proxy_file = input(Colorate.Vertical(Colors.blue_to_purple, "Proxy file: "))
        with open(proxy_file, 'r') as f:
          proxies = f.read().splitlines()
        proxy_dict = {
            "http": "http://" + random.choice(proxies),
            "https": "https://" + random.choice(proxies)
        }
    else:
        proxy_dict = None

    print(Colorate.Vertical(Colors.green_to_blue,"")) 

    def genrandomidd(): 
        return ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for _ in range(30)) 

    def randomname(): 
        return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(8)) 

    games = ['', 'confessions', '3words', 'wfriendship', 'rizzme', 'tbh', 'shipme', 'yourcrush', 'cancelled', 'dealbreaker'] 
    gameslugg = random.choice(games) 
    randomdeviceid = genrandomidd() 

    value =0 
    notsend =0 

    def send_request(): 
        nonlocal value 
        nonlocal notsend 

    while value < Count:
    
            headers = { 
                'Host': 'ngl.link', 
                'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"', 
                'accept': '*/*', 
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 
                'x-requested-with': 'XMLHttpRequest', 
                'sec-ch-ua-mobile': '?0', 
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36', 
                'sec-ch-ua-platform': '"Windows"', 
                'origin': 'https://ngl.link', 
                'sec-fetch-site': 'same-origin', 
                'sec-fetch-mode': 'cors', 
                'sec-fetch-dest': 'empty', 
                'referer': f'https://ngl.link/{nglusername}', 
                'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7', 
            } 

            data = { 
                'username': f'{nglusername}', 
                'question': f'{message}', 
                'deviceId': randomdeviceid, 
                'gameSlug': gameslugg, 
                'referrer': '', 
            } 

            try: 
                response = requests.post('https://ngl.link/api/submit', headers=headers, data=data, proxies=proxy_dict)
                if response.status_code == 200: 
                    notsend = 0 
                    value += 1 
                    print(G+"[✔]"+W+"Send =>"+G+"{}".format(value)+W) 
                elif response.status_code == 429: 
                    retry_after = float(response.headers.get("Retry-After", "5")) 
                    print(R+"Rate limit reached. Waiting for retry... ({} seconds)\033[0m".format(retry_after)) 
                    time.sleep(retry_after) 
                else: 
                    notsend += 1 
                    print(R+"[✘]"+W+"Not Send") 
                if notsend == 10: 
                    print(R+"[✘]"+W+"Wait 5 Seconds") 
                    time.sleep(5) 
                    notsend = 0 
            except: 
                print(R+"[✘]"+W+"Proxy Error") 

    threads = [] 
    for i in range(num_threads): 
        t = threading.Thread(target=send_request) 
        threads.append(t) 
        t.start() 

    for t in threads: 
        t.join() 

def main():

    RPC = ConfigurationRPC()
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(2)

    print(Colorate.Vertical(Colors.blue_to_purple,"""

 ██▒   █▓ ██▓ ▒█████   ██▓    ▓█████▄▄▄█████▓ 
▓██░   █▒▓██▒▒██▒  ██▒▓██▒    ▓█   ▀▓  ██▒ ▓▒ 
 ▓██  █▒░▒██▒▒██░  ██▒▒██░    ▒███  ▒ ▓██░ ▒░ 
  ▒██ █░░░██░▒██   ██░▒██░    ▒▓█  ▄░ ▓██▓ ░  
   ▒▀█░  ░██░░ ████▓▒░░██████▒░▒████▒ ▒██▒ ░   
   ░ ▐░  ░▓  ░ ▒░▒░▒░ ░ ▒░▓  ░░░ ▒░ ░ ▒ ░░    
                Hisako Domina                            
    """))

    print(Colorate.Diagonal(Colors.blue_to_purple,"                   1. CUSTOM SPAM"))
    print(Colorate.Diagonal(Colors.blue_to_purple,"                   2. DELETE INBOX"))
    choice = input(Colorate.Diagonal(Colors.blue_to_purple,"                   ~~> "))

    if choice == '1':
        CustomSpam()
    if choice == '2':
        sendspam() 
  
if __name__ == "__main__":
    main()
