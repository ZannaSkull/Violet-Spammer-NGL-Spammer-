from pypresence import Presence
import requests 
import os 
import ctypes
from pystyle import *
import time
import random
def ConfigurationRPC():
    RPC = Presence(client_id="1169401122469986388")
    RPC.connect()
    RPC.update(
        state="UwU | Spamming on NGL",
        details="That's legal",
        large_image="uwuspam",
        large_text="Destroying some pussy's"
    )
    return RPC

color_combinations = [
    Colors.cyan_to_blue,
    Colors.purple_to_blue,
    Colors.red_to_purple,
    # Add more color combinations as needed
]
def set_console_title(title):
    title_bytes = title.encode('cp1252')
    ctypes.windll.kernel32.SetConsoleTitleA(title_bytes)

random_color_combination = random.choice(color_combinations)
def custom_spam():
    R = '\033[31m'
    G = '\033[32m'
    W = '\033[0m'    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Diagonal(random_color_combination,"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⣸⣿⣿⣷⣄⠀⠀⠀⠀⣀⡀⠀⠀⠀⢀⣠⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⡿⣿⣿⣷⣦⣴⣿⣿⣿⣄⣠⠶⣿⡿⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⡿⠿⢛⣿⣿⣿⣷⣮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣯⠽⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠈⠛⠻⠿⣽⣿⣿⣿⢻⣿⡹⣶⡾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⢟⣾⢏⡤⠴⠶⠆⠀⠀⠀⠀⠀⠤⠤⣄⣻⣿⣿⣾⡏⣷⠽⣿⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣧⣾⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢹⣿⣿⣿⡇⣿⣷⣿⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠿⠛⣿⣿⣿⣠⣤⡴⣦⣝⣦⠀⠀⠀⠀⠖⣋⣡⣤⣸⡇⢻⣿⣿⣿⣿⣼⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⣿⣿⣧⠟⢁⣠⣄⡉⠹⠀⠀⠀⠀⠚⠉⢹⡉⠙⠻⣦⣿⣿⣯⣭⡿⢦⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⣿⣦⣮⣶⣷⣽⣤⠀⠀⠀⠀⣰⣯⣅⡙⢧⠀⢹⣿⣿⣿⣿⣇⠀⠹⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣋⣿⡇⠈⢻⣿⣿⠿⠁⠀⠀⠀⠀⠻⣿⣿⣿⣿⠁⠀⣾⣿⡆⣀⡌⢧⠀⠘⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣬⣹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⢰⣿⣿⣿⠙⡆⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⣽⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡟⣿⣿⡏⣡⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀Deobfuscated by Overpower⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡿⢳⡀⠀⠀⠀⠀⠐⢶⠀⠀⠀⠀⠀⠀⠀⣸⣿⡇⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Hisako Daddy⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠶⣿⣿⣇⣿⢻⣿⠀⠀⠀⠀          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠻⣿⣿⣿⣷⡙⠦⣤⡀⠀⢀⣠⡤⠖⠛⣡⣾⣿⣿⣿⣿⠈⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⢹⣿⢻⣿⣿⣦⣌⡉⠉⠉⢀⣀⣠⣾⣿⣿⣿⡏⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡏⠀⣹⣿⣿⣿⡏⠀⢸⣿⣿⣿⣿⣿⣯⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⡼⠁⡿⣿⣿⣧⣀⣜⣿⣿⡿⢟⣡⡞⠀⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⣸⣿⡿⢿⣴⣿⣿⣷⣶⣿⣿⣿⠁⠀⠀⠈⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⢀⣿⢷⣶⣿⠋⠙⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⣿⠹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⠀⠀⣼⣿⠸⣿⣧⣀⣴⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⣿⠀⠘⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠛⠀⣠⣾⣿⣿⡇⣿⣿⣿⣿⣿⡏⠀⠀⢹⠀⠀⠀⠀⢀⡇⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⢠⣾⣿⣿⣿⡿⣱⣿⣿⣿⣿⣿⠃⠉⠉⡟⠀⠀⠀⠀⢸⠁⠀⠀⣼⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⢰⣿⣿⣿⣿⣟⣵⣿⠿⢿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢸⠀⢀⡼⠁⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                             [UWU SPAMMER]
    """))
    
    nglusername = input(Colorate.Diagonal(random_color_combination, "\nUsername: "))
    message = input(Colorate.Diagonal(random_color_combination,"Message: "))
    Count = int(input(Colorate.Diagonal(random_color_combination,"Amount: ")))
    print("\n")
    games = ['', 'confessions', '3words', 'wfriendship', 'rizzme', 'tbh', 'shipme', 'yourcrush', 'cancelled', 'dealbreaker']
    game_slug = random.choice(games)
    value = 0
    notsend = 0
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
        random_device_id = generate_random_device_id()
        random_generated_username = generate_random_username()
        data = {
            'username': f'{nglusername}',
            'question': f'{message}',
            'deviceId': random_device_id,
            'gameSlug': game_slug,
            'referrer': '',
        }
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"  [✔]"+W+f"Successfully sent to {nglusername}")
        else:
            notsend += 1
            print(R+"  [✘]"+W+"Not Sent")
        if notsend == 10:
            print(R+"  [↻]"+W+"Retrying...")
            time.sleep(5)
            notsend = 0
    input(G+"\n\n  [⌂]"+W+"Spamming completed, press any key to go back to menu") 
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
def heart_spam():
    R = '\033[31m'
    G = '\033[32m'
    W = '\033[0m'
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(Colorate.Diagonal(random_color_combination,"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⣸⣿⣿⣷⣄⠀⠀⠀⠀⣀⡀⠀⠀⠀⢀⣠⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⡿⣿⣿⣷⣦⣴⣿⣿⣿⣄⣠⠶⣿⡿⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⡿⠿⢛⣿⣿⣿⣷⣮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣯⠽⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠈⠛⠻⠿⣽⣿⣿⣿⢻⣿⡹⣶⡾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⢟⣾⢏⡤⠴⠶⠆⠀⠀⠀⠀⠀⠤⠤⣄⣻⣿⣿⣾⡏⣷⠽⣿⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣧⣾⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢹⣿⣿⣿⡇⣿⣷⣿⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠿⠛⣿⣿⣿⣠⣤⡴⣦⣝⣦⠀⠀⠀⠀⠖⣋⣡⣤⣸⡇⢻⣿⣿⣿⣿⣼⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⣿⣿⣧⠟⢁⣠⣄⡉⠹⠀⠀⠀⠀⠚⠉⢹⡉⠙⠻⣦⣿⣿⣯⣭⡿⢦⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⣿⣦⣮⣶⣷⣽⣤⠀⠀⠀⠀⣰⣯⣅⡙⢧⠀⢹⣿⣿⣿⣿⣇⠀⠹⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣋⣿⡇⠈⢻⣿⣿⠿⠁⠀⠀⠀⠀⠻⣿⣿⣿⣿⠁⠀⣾⣿⡆⣀⡌⢧⠀⠘⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣬⣹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⢰⣿⣿⣿⠙⡆⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⣽⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡟⣿⣿⡏⣡⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀Deobfuscated by Overpower⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡿⢳⡀⠀⠀⠀⠀⠐⢶⠀⠀⠀⠀⠀⠀⠀⣸⣿⡇⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Hisako Daddy⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠶⣿⣿⣇⣿⢻⣿⠀⠀⠀⠀          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠻⣿⣿⣿⣷⡙⠦⣤⡀⠀⢀⣠⡤⠖⠛⣡⣾⣿⣿⣿⣿⠈⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⢹⣿⢻⣿⣿⣦⣌⡉⠉⠉⢀⣀⣠⣾⣿⣿⣿⡏⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡏⠀⣹⣿⣿⣿⡏⠀⢸⣿⣿⣿⣿⣿⣯⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⡼⠁⡿⣿⣿⣧⣀⣜⣿⣿⡿⢟⣡⡞⠀⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⣸⣿⡿⢿⣴⣿⣿⣷⣶⣿⣿⣿⠁⠀⠀⠈⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⢀⣿⢷⣶⣿⠋⠙⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⣿⠹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⠀⠀⣼⣿⠸⣿⣧⣀⣴⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⣿⠀⠘⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠛⠀⣠⣾⣿⣿⡇⣿⣿⣿⣿⣿⡏⠀⠀⢹⠀⠀⠀⠀⢀⡇⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⢠⣾⣿⣿⣿⡿⣱⣿⣿⣿⣿⣿⠃⠉⠉⡟⠀⠀⠀⠀⢸⠁⠀⠀⣼⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⢰⣿⣿⣿⣿⣟⣵⣿⠿⢿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢸⠀⢀⡼⠁⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                             [UWU SPAMMER]
    """))
    nglusername = input(Colorate.Diagonal(random_color_combination, "Username: "))
    Count = int(input(Colorate.Diagonal(random_color_combination,"Amount: ")))
    print("")
    value = 0
    notsend = 0
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
        random_device_id = generate_random_device_id()
        random_generated_username = generate_random_username()
        data = {
            'username': f'{nglusername}',
            'question': f'♥️♥️♥️♥️♥️♥️♥️♥️♥️♥️♥️♥️♥️♥️💗💗💗💗💗💗💗💗💗💗💗💗💗💗💕💕💕💕💕💕',
            'deviceId': random_device_id,
            'gameSlug': 'confessions',
            'referrer': '',
        }
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"  [✔]"+W+f"Successfully sent to {nglusername}")
        else:
            notsend += 1
            print(R+"  [✘]"+W+"Not Sent")
        if notsend == 10:
            print(R+"  [↻]"+W+"Retrying...")
            time.sleep(5)
            notsend = 0
    input(G+"  [⌂]"+W+"Spamming completed, press any key to go back to menu") 
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
  
def fuck_spam():
    R = '\033[31m'
    G = '\033[32m'
    W = '\033[0m'
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Diagonal(random_color_combination,"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⣸⣿⣿⣷⣄⠀⠀⠀⠀⣀⡀⠀⠀⠀⢀⣠⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⡿⣿⣿⣷⣦⣴⣿⣿⣿⣄⣠⠶⣿⡿⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⡿⠿⢛⣿⣿⣿⣷⣮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣯⠽⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠈⠛⠻⠿⣽⣿⣿⣿⢻⣿⡹⣶⡾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⢟⣾⢏⡤⠴⠶⠆⠀⠀⠀⠀⠀⠤⠤⣄⣻⣿⣿⣾⡏⣷⠽⣿⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣧⣾⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢹⣿⣿⣿⡇⣿⣷⣿⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠿⠛⣿⣿⣿⣠⣤⡴⣦⣝⣦⠀⠀⠀⠀⠖⣋⣡⣤⣸⡇⢻⣿⣿⣿⣿⣼⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⣿⣿⣧⠟⢁⣠⣄⡉⠹⠀⠀⠀⠀⠚⠉⢹⡉⠙⠻⣦⣿⣿⣯⣭⡿⢦⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⣿⣦⣮⣶⣷⣽⣤⠀⠀⠀⠀⣰⣯⣅⡙⢧⠀⢹⣿⣿⣿⣿⣇⠀⠹⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣋⣿⡇⠈⢻⣿⣿⠿⠁⠀⠀⠀⠀⠻⣿⣿⣿⣿⠁⠀⣾⣿⡆⣀⡌⢧⠀⠘⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣬⣹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⢰⣿⣿⣿⠙⡆⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⣽⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡟⣿⣿⡏⣡⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀Deobfuscated by Overpower⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡿⢳⡀⠀⠀⠀⠀⠐⢶⠀⠀⠀⠀⠀⠀⠀⣸⣿⡇⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Hisako Daddy⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠶⣿⣿⣇⣿⢻⣿⠀⠀⠀⠀          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠻⣿⣿⣿⣷⡙⠦⣤⡀⠀⢀⣠⡤⠖⠛⣡⣾⣿⣿⣿⣿⠈⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⢹⣿⢻⣿⣿⣦⣌⡉⠉⠉⢀⣀⣠⣾⣿⣿⣿⡏⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡏⠀⣹⣿⣿⣿⡏⠀⢸⣿⣿⣿⣿⣿⣯⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⡼⠁⡿⣿⣿⣧⣀⣜⣿⣿⡿⢟⣡⡞⠀⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⣸⣿⡿⢿⣴⣿⣿⣷⣶⣿⣿⣿⠁⠀⠀⠈⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⢀⣿⢷⣶⣿⠋⠙⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⣿⠹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⠀⠀⣼⣿⠸⣿⣧⣀⣴⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⣿⠀⠘⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠛⠀⣠⣾⣿⣿⡇⣿⣿⣿⣿⣿⡏⠀⠀⢹⠀⠀⠀⠀⢀⡇⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⢠⣾⣿⣿⣿⡿⣱⣿⣿⣿⣿⣿⠃⠉⠉⡟⠀⠀⠀⠀⢸⠁⠀⠀⣼⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⢰⣿⣿⣿⣿⣟⣵⣿⠿⢿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢸⠀⢀⡼⠁⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                             [UWU SPAMMER]
    """))
    nglusername = input(Colorate.Diagonal(random_color_combination, "Username: "))
    Count = int(input(Colorate.Diagonal(random_color_combination,"Amount: ")))
    print("")
    games = ['', 'confessions', '3words', 'wfriendship', 'rizzme', 'tbh', 'shipme', 'yourcrush', 'cancelled', 'dealbreaker']
    game_slug = random.choice(games)
    value = 0
    notsend = 0
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
        random_device_id = generate_random_device_id()
        random_generated_username = generate_random_username()
        question = ('''
⠀⠀⠀⠀⠀⠀⠀ ⢀⡤⠤⣄⠀⠀⠀⠀⠀⠀⠀ 
 ⠀⠀⠀⠀⠀⠀⠀⣾⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀ 
 ⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀ 
 ⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀ 
 ⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀  
 ⠀⠀⠀⢀⡾⠋⠻⡇⠀⠀⢸⣧⣀⡀⠀⠀⠀⠀ 
 ⠀⠀⢀⣾⠁⠀⠀⡇⠀⠀⢸⠁⠀⢹⣀⠀⠀⠀ 
 ⢀⡴⠋⡟⠀⠀⢠⡇⠀⠀⢸⠀⠀⠀⡇⠉⢆⠀ 
 ⡎⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠈⣆ 
 ⢷⡀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸ 
 ⠀⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾ 
 ⠀⠀⠈⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁ 
 ⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⢰⠋⠀⠀ 
 ⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀ 
 ⠀⠀⠀⠀⠀⠛⠒⠒⠒⠒⠒⠒⠒⠚⠃⠀⠀⠀
  ᶠYͧoͨᵏuᶠYͧoͨᵏu | OWN SPAMMER ''')
        data = {
            'username': f'{nglusername}',
            'question': question,
            'deviceId': {random_device_id},
            'gameSlug': game_slug,
            'referrer': '',
        }

        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"  [✔]"+W+f"Successfully sent to {nglusername}")
        else:
            notsend += 1
            print(R+"  [✘]"+W+"Not Sent")
        if notsend == 10:
            print(R+"  [↻]"+W+"Retrying...")
            time.sleep(5)
            notsend = 0
    
    input(G+"  [⌂]"+W+"Spamming completed, press any key to go back to menu") 
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
def sex_spam():

    R = '\033[31m'
    G = '\033[32m'
    W = '\033[0m'

    os.system('cls' if os.name == 'nt' else 'clear')

    print(Colorate.Diagonal(random_color_combination,"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⣸⣿⣿⣷⣄⠀⠀⠀⠀⣀⡀⠀⠀⠀⢀⣠⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⡿⣿⣿⣷⣦⣴⣿⣿⣿⣄⣠⠶⣿⡿⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⡿⠿⢛⣿⣿⣿⣷⣮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣯⠽⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠈⠛⠻⠿⣽⣿⣿⣿⢻⣿⡹⣶⡾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⢟⣾⢏⡤⠴⠶⠆⠀⠀⠀⠀⠀⠤⠤⣄⣻⣿⣿⣾⡏⣷⠽⣿⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣧⣾⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢹⣿⣿⣿⡇⣿⣷⣿⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠿⠛⣿⣿⣿⣠⣤⡴⣦⣝⣦⠀⠀⠀⠀⠖⣋⣡⣤⣸⡇⢻⣿⣿⣿⣿⣼⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⣿⣿⣧⠟⢁⣠⣄⡉⠹⠀⠀⠀⠀⠚⠉⢹⡉⠙⠻⣦⣿⣿⣯⣭⡿⢦⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⣿⣦⣮⣶⣷⣽⣤⠀⠀⠀⠀⣰⣯⣅⡙⢧⠀⢹⣿⣿⣿⣿⣇⠀⠹⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣋⣿⡇⠈⢻⣿⣿⠿⠁⠀⠀⠀⠀⠻⣿⣿⣿⣿⠁⠀⣾⣿⡆⣀⡌⢧⠀⠘⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣬⣹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⢰⣿⣿⣿⠙⡆⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⣽⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡟⣿⣿⡏⣡⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀Deobfuscated by Overpower
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡿⢳⡀⠀⠀⠀⠀⠐⢶⠀⠀⠀⠀⠀⠀⠀⣸⣿⡇⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Hisako Daddy⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠶⣿⣿⣇⣿⢻⣿⠀⠀⠀⠀          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠻⣿⣿⣿⣷⡙⠦⣤⡀⠀⢀⣠⡤⠖⠛⣡⣾⣿⣿⣿⣿⠈⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⢹⣿⢻⣿⣿⣦⣌⡉⠉⠉⢀⣀⣠⣾⣿⣿⣿⡏⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡏⠀⣹⣿⣿⣿⡏⠀⢸⣿⣿⣿⣿⣿⣯⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⡼⠁⡿⣿⣿⣧⣀⣜⣿⣿⡿⢟⣡⡞⠀⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⣸⣿⡿⢿⣴⣿⣿⣷⣶⣿⣿⣿⠁⠀⠀⠈⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⢀⣿⢷⣶⣿⠋⠙⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⣿⠹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⠀⠀⣼⣿⠸⣿⣧⣀⣴⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⣿⠀⠘⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠛⠀⣠⣾⣿⣿⡇⣿⣿⣿⣿⣿⡏⠀⠀⢹⠀⠀⠀⠀⢀⡇⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⢠⣾⣿⣿⣿⡿⣱⣿⣿⣿⣿⣿⠃⠉⠉⡟⠀⠀⠀⠀⢸⠁⠀⠀⣼⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⢰⣿⣿⣿⣿⣟⣵⣿⠿⢿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢸⠀⢀⡼⠁⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                             [UWU SPAMMER]

    """))

    nglusername = input(Colorate.Diagonal(random_color_combination, "Username: "))
    Count = int(input(Colorate.Diagonal(random_color_combination,"Amount: ")))


    print("")

    games = ['', 'confessions', '3words', 'wfriendship', 'rizzme', 'tbh', 'shipme', 'yourcrush', 'cancelled', 'dealbreaker']
    game_slug = random.choice(games)


    value = 0
    notsend = 0
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

        random_device_id = generate_random_device_id()
        random_generated_username = generate_random_username()

        question = ('''
⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢺⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⡗⠉⠀⠀⠀⠀⠀⠀⠀⣠⣠⣤⠀⠀⠀
⠀⣞⠉⢁⡀⠹⣄⠀⠀⠀⠀⢠⣿⠀⢀⠃⠀⠀
⠀⣻⡇⠸⡇⢸⣎⠳⠤⠤⢤⠴⠾⠏⢑⣒⣒⣒
⠀⢹⢻⡄⢿⣌⠈⠉⠈⣽⠏⠀⠀⢺⢱⣤⣠⣢
⢀⠞⠀⠙⠳⣝⢦⣴⣻⡅⢀⣀⠖⠋⠀⠀⠀⠀
⢸⡀⠀⠀⢰⡟⠻⠦⣽⡷⠋⠁⠀⠀⠀⠀⠀⠀
⠀⠙⣄⠀⠈⣷⡀⠀⢯⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠹⣆⠀⢸⣷⡄⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⠟⢀⡾⠁⣻⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢰⡇⢀⡾⠁⠀⠉⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⢁⣻⣓⣲⢦⣻⣮⣀⣀⠀⠀⠀⠀⠀⠀⠀
⠀⢯⣘⠣⢄⡀⠰⢧⣽⣻⣯⠀⠀    

        ''')
        data = {
            'username': f'{nglusername}',
            'question': question,
            'deviceId': {random_device_id},
            'gameSlug': game_slug,
            'referrer': '',
        }



        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"  [✔]"+W+f"Successfully sent to {nglusername}")
        else:
            notsend += 1
            print(R+"  [✘]"+W+"Not Sent")
        if notsend == 10:
            print(R+"  [↻]"+W+"Retrying...")
            time.sleep(5)
            notsend = 0

    

    input(G+"  [⌂]"+W+"Spamming completed, press any key to go back to menu") 
    os.system('cls' if os.name == 'nt' else 'clear')
    main()

def nazi_spam():

    R = '\033[31m'
    G = '\033[32m'
    W = '\033[0m'

    os.system('cls' if os.name == 'nt' else 'clear')

    print(Colorate.Diagonal(random_color_combination,"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⣸⣿⣿⣷⣄⠀⠀⠀⠀⣀⡀⠀⠀⠀⢀⣠⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⡿⣿⣿⣷⣦⣴⣿⣿⣿⣄⣠⠶⣿⡿⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⡿⠿⢛⣿⣿⣿⣷⣮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣯⠽⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠈⠛⠻⠿⣽⣿⣿⣿⢻⣿⡹⣶⡾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⢟⣾⢏⡤⠴⠶⠆⠀⠀⠀⠀⠀⠤⠤⣄⣻⣿⣿⣾⡏⣷⠽⣿⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣧⣾⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢹⣿⣿⣿⡇⣿⣷⣿⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠿⠛⣿⣿⣿⣠⣤⡴⣦⣝⣦⠀⠀⠀⠀⠖⣋⣡⣤⣸⡇⢻⣿⣿⣿⣿⣼⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⣿⣿⣧⠟⢁⣠⣄⡉⠹⠀⠀⠀⠀⠚⠉⢹⡉⠙⠻⣦⣿⣿⣯⣭⡿⢦⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⣿⣦⣮⣶⣷⣽⣤⠀⠀⠀⠀⣰⣯⣅⡙⢧⠀⢹⣿⣿⣿⣿⣇⠀⠹⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣋⣿⡇⠈⢻⣿⣿⠿⠁⠀⠀⠀⠀⠻⣿⣿⣿⣿⠁⠀⣾⣿⡆⣀⡌⢧⠀⠘⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣬⣹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⢰⣿⣿⣿⠙⡆⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⣽⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡟⣿⣿⡏⣡⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀Deobfuscated by Overpower
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡿⢳⡀⠀⠀⠀⠀⠐⢶⠀⠀⠀⠀⠀⠀⠀⣸⣿⡇⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Hisako Daddy⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠶⣿⣿⣇⣿⢻⣿⠀⠀⠀⠀          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠻⣿⣿⣿⣷⡙⠦⣤⡀⠀⢀⣠⡤⠖⠛⣡⣾⣿⣿⣿⣿⠈⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⢹⣿⢻⣿⣿⣦⣌⡉⠉⠉⢀⣀⣠⣾⣿⣿⣿⡏⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡏⠀⣹⣿⣿⣿⡏⠀⢸⣿⣿⣿⣿⣿⣯⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⡼⠁⡿⣿⣿⣧⣀⣜⣿⣿⡿⢟⣡⡞⠀⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⣸⣿⡿⢿⣴⣿⣿⣷⣶⣿⣿⣿⠁⠀⠀⠈⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⢀⣿⢷⣶⣿⠋⠙⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⣿⠹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⠀⠀⣼⣿⠸⣿⣧⣀⣴⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⣿⠀⠘⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠛⠀⣠⣾⣿⣿⡇⣿⣿⣿⣿⣿⡏⠀⠀⢹⠀⠀⠀⠀⢀⡇⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⢠⣾⣿⣿⣿⡿⣱⣿⣿⣿⣿⣿⠃⠉⠉⡟⠀⠀⠀⠀⢸⠁⠀⠀⣼⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⢰⣿⣿⣿⣿⣟⣵⣿⠿⢿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢸⠀⢀⡼⠁⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                             [UWU SPAMMER]

    """))

    nglusername = input(Colorate.Diagonal(random_color_combination, "Username: "))
    Count = int(input(Colorate.Diagonal(random_color_combination,"Amount: ")))


    print("")

    games = ['', 'confessions', '3words', 'wfriendship', 'rizzme', 'tbh', 'shipme', 'yourcrush', 'cancelled', 'dealbreaker']
    game_slug = random.choice(games)


    value = 0
    notsend = 0
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

        random_device_id = generate_random_device_id()
        random_generated_username = generate_random_username()

        question = ('''
⬛⬛⬛⬛⬜⬜⬛
⬜⬜⬜⬛⬜⬜⬛
⬜⬜⬜⬛⬜⬜⬛
⬛⬛⬛⬛⬛⬛⬛
⬛⬜⬜⬛⬜⬜⬜
⬛⬜⬜⬛⬜⬜⬜
⬛⬜⬜⬛⬛⬛⬛⠀⠀⠀
        ''')
        data = {
            'username': f'{nglusername}',
            'question': question,
            'deviceId': {random_device_id},
            'gameSlug': game_slug,
            'referrer': '',
        }



        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"  [✔]"+W+f"Successfully sent to {nglusername}")
        else:
            notsend += 1
            print(R+"  [✘]"+W+"Not Sent")
        if notsend == 10:
            print(R+"  [↻]"+W+"Retrying...")
            time.sleep(5)
            notsend = 0

    

    input(G+"  [⌂]"+W+"Spamming completed, press any key to go back to menu") 
    os.system('cls' if os.name == 'nt' else 'clear')
    main()

def generate_random_device_id():
    return ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for _ in range(30))

def generate_random_username():
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(8))

def send_request_with_given_and_random_username(username):
    games = ['', 'confessions', '3words', 'wfriendship', 'rizzme', 'tbh', 'shipme', 'yourcrush', 'cancelled', 'dealbreaker']
    game_slug = random.choice(games)
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
    random_device_id = generate_random_device_id()
    random_generated_username = generate_random_username()
    
    data = {
        "username": username,
        "question": question,
        "deviceId": random_device_id,
        "gameSlug": game_slug
    }
    response = requests.post(url, data=data, headers=headers)
    return username, random_generated_username

def send_requests_with_given_and_random_username():
    input_username = input("Username")
    while True:
        username, random_username = send_request_with_given_and_random_username(input_username)
        print("Inbox deleter exploit sent")
        time.sleep(1)  
def curse_spam():
    R = '\033[31m'
    G = '\033[32m'
    W = '\033[0m'
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Diagonal(random_color_combination,"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⣸⣿⣿⣷⣄⠀⠀⠀⠀⣀⡀⠀⠀⠀⢀⣠⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⡿⣿⣿⣷⣦⣴⣿⣿⣿⣄⣠⠶⣿⡿⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⡿⠿⢛⣿⣿⣿⣷⣮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣯⠽⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠈⠛⠻⠿⣽⣿⣿⣿⢻⣿⡹⣶⡾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⢟⣾⢏⡤⠴⠶⠆⠀⠀⠀⠀⠀⠤⠤⣄⣻⣿⣿⣾⡏⣷⠽⣿⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣧⣾⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢹⣿⣿⣿⡇⣿⣷⣿⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠿⠛⣿⣿⣿⣠⣤⡴⣦⣝⣦⠀⠀⠀⠀⠖⣋⣡⣤⣸⡇⢻⣿⣿⣿⣿⣼⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⣿⣿⣧⠟⢁⣠⣄⡉⠹⠀⠀⠀⠀⠚⠉⢹⡉⠙⠻⣦⣿⣿⣯⣭⡿⢦⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⣿⣦⣮⣶⣷⣽⣤⠀⠀⠀⠀⣰⣯⣅⡙⢧⠀⢹⣿⣿⣿⣿⣇⠀⠹⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣋⣿⡇⠈⢻⣿⣿⠿⠁⠀⠀⠀⠀⠻⣿⣿⣿⣿⠁⠀⣾⣿⡆⣀⡌⢧⠀⠘⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣬⣹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⢰⣿⣿⣿⠙⡆⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⣽⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡟⣿⣿⡏⣡⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀Deobfuscated by Overpower⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡿⢳⡀⠀⠀⠀⠀⠐⢶⠀⠀⠀⠀⠀⠀⠀⣸⣿⡇⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Hisako Daddy⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠶⣿⣿⣇⣿⢻⣿⠀⠀⠀⠀          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠻⣿⣿⣿⣷⡙⠦⣤⡀⠀⢀⣠⡤⠖⠛⣡⣾⣿⣿⣿⣿⠈⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⢹⣿⢻⣿⣿⣦⣌⡉⠉⠉⢀⣀⣠⣾⣿⣿⣿⡏⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡏⠀⣹⣿⣿⣿⡏⠀⢸⣿⣿⣿⣿⣿⣯⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⡼⠁⡿⣿⣿⣧⣀⣜⣿⣿⡿⢟⣡⡞⠀⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⣸⣿⡿⢿⣴⣿⣿⣷⣶⣿⣿⣿⠁⠀⠀⠈⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⢀⣿⢷⣶⣿⠋⠙⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⣿⠹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⠀⠀⣼⣿⠸⣿⣧⣀⣴⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⣿⠀⠘⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠛⠀⣠⣾⣿⣿⡇⣿⣿⣿⣿⣿⡏⠀⠀⢹⠀⠀⠀⠀⢀⡇⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⢠⣾⣿⣿⣿⡿⣱⣿⣿⣿⣿⣿⠃⠉⠉⡟⠀⠀⠀⠀⢸⠁⠀⠀⣼⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⢰⣿⣿⣿⣿⣟⣵⣿⠿⢿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢸⠀⢀⡼⠁⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                             [UWU SPAMMER]    """))

    games = ['', 'confessions', '3words', 'wfriendship', 'rizzme', 'tbh', 'shipme', 'yourcrush', 'cancelled', 'dealbreaker']
    game_slug = random.choice(games)
    nglusername = input(Colorate.Diagonal(random_color_combination, "Username: "))
    Count = int(input(Colorate.Diagonal(random_color_combination,"Amount: ")))

    
    print("")
    value = 0
    notsend = 0
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
        random_device_id = generate_random_device_id()
        random_generated_username = generate_random_username()
        data = {
            'username': f'{nglusername}',
            'question': f'🗿🗿🗿🗿🗿🗿🗿🗿',
            'deviceId': random_device_id,
            'gameSlug': game_slug,
            'referrer': '',
        }
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"  [✔]"+W+f"Successfully sent to {nglusername}")
        else:
            notsend += 1
            print(R+"  [✘]"+W+"Not Sent")
        if notsend == 10:
            print(R+"  [↻]"+W+"Retrying...")
            time.sleep(5)
            notsend = 0
    input(G+"  [⌂]"+W+"Spamming completed, press any key to go back to menu") 
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
def generate_random_device_id():
    return ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for _ in range(30))
def generate_random_username():
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(8))
def send_request_with_given_and_random_username(username):
    games = ['', 'confessions', '3words', 'wfriendship', 'rizzme', 'tbh', 'shipme', 'yourcrush', 'cancelled', 'dealbreaker']
    game_slug = random.choice(games)
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
    random_device_id = generate_random_device_id()
    random_generated_username = generate_random_username()
    
    data = {
        "username": username,
        "question": question,
        "deviceId": random_device_id,
        "gameSlug": game_slug
    }
    response = requests.post(url, data=data, headers=headers)
    return username, random_generated_username


def send_requests_with_given_and_random_username():
    R = '\033[31m'
    G = '\033[32m'
    W = '\033[0m'
    P = '\033[38;5;92m'
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Diagonal(random_color_combination,"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⣸⣿⣿⣷⣄⠀⠀⠀⠀⣀⡀⠀⠀⠀⢀⣠⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⡿⣿⣿⣷⣦⣴⣿⣿⣿⣄⣠⠶⣿⡿⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⡿⠿⢛⣿⣿⣿⣷⣮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣯⠽⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠈⠛⠻⠿⣽⣿⣿⣿⢻⣿⡹⣶⡾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⢟⣾⢏⡤⠴⠶⠆⠀⠀⠀⠀⠀⠤⠤⣄⣻⣿⣿⣾⡏⣷⠽⣿⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣧⣾⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢹⣿⣿⣿⡇⣿⣷⣿⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠿⠛⣿⣿⣿⣠⣤⡴⣦⣝⣦⠀⠀⠀⠀⠖⣋⣡⣤⣸⡇⢻⣿⣿⣿⣿⣼⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⣿⣿⣧⠟⢁⣠⣄⡉⠹⠀⠀⠀⠀⠚⠉⢹⡉⠙⠻⣦⣿⣿⣯⣭⡿⢦⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⣿⣦⣮⣶⣷⣽⣤⠀⠀⠀⠀⣰⣯⣅⡙⢧⠀⢹⣿⣿⣿⣿⣇⠀⠹⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣋⣿⡇⠈⢻⣿⣿⠿⠁⠀⠀⠀⠀⠻⣿⣿⣿⣿⠁⠀⣾⣿⡆⣀⡌⢧⠀⠘⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣬⣹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⢰⣿⣿⣿⠙⡆⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⣽⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡟⣿⣿⡏⣡⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀Deobfuscated by Overpower⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡿⢳⡀⠀⠀⠀⠀⠐⢶⠀⠀⠀⠀⠀⠀⠀⣸⣿⡇⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Hisako Daddy⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠶⣿⣿⣇⣿⢻⣿⠀⠀⠀⠀          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠻⣿⣿⣿⣷⡙⠦⣤⡀⠀⢀⣠⡤⠖⠛⣡⣾⣿⣿⣿⣿⠈⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⢹⣿⢻⣿⣿⣦⣌⡉⠉⠉⢀⣀⣠⣾⣿⣿⣿⡏⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡏⠀⣹⣿⣿⣿⡏⠀⢸⣿⣿⣿⣿⣿⣯⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⡼⠁⡿⣿⣿⣧⣀⣜⣿⣿⡿⢟⣡⡞⠀⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⣸⣿⡿⢿⣴⣿⣿⣷⣶⣿⣿⣿⠁⠀⠀⠈⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⢀⣿⢷⣶⣿⠋⠙⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⣿⠹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⠀⠀⣼⣿⠸⣿⣧⣀⣴⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⣿⠀⠘⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠛⠀⣠⣾⣿⣿⡇⣿⣿⣿⣿⣿⡏⠀⠀⢹⠀⠀⠀⠀⢀⡇⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⢠⣾⣿⣿⣿⡿⣱⣿⣿⣿⣿⣿⠃⠉⠉⡟⠀⠀⠀⠀⢸⠁⠀⠀⣼⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⢰⣿⣿⣿⣿⣟⣵⣿⠿⢿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢸⠀⢀⡼⠁⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                             [UWU SPAMMER]
    """))    
    input_username = input(Colorate.Diagonal(random_color_combination, "Username: "))
    print("")
    while True:
        username, random_username = send_request_with_given_and_random_username(input_username)
        print(G+"  [✔]"+W+f"Inbox deleter exploit sent to {username}")
        time.sleep(1)
def main():
    R = '\033[31m'
    G = '\033[32m'
    W = '\033[0m'
    P = '\033[38;5;92m'
    set_console_title("NGL Spammer | UWU")
    RPC = ConfigurationRPC()
    
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(2)
    print(Colorate.Diagonal(random_color_combination,"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⣸⣿⣿⣷⣄⠀⠀⠀⠀⣀⡀⠀⠀⠀⢀⣠⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⡿⣿⣿⣷⣦⣴⣿⣿⣿⣄⣠⠶⣿⡿⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⡿⠿⢛⣿⣿⣿⣷⣮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣯⠽⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠈⠛⠻⠿⣽⣿⣿⣿⢻⣿⡹⣶⡾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⢟⣾⢏⡤⠴⠶⠆⠀⠀⠀⠀⠀⠤⠤⣄⣻⣿⣿⣾⡏⣷⠽⣿⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣧⣾⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢹⣿⣿⣿⡇⣿⣷⣿⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠿⠛⣿⣿⣿⣠⣤⡴⣦⣝⣦⠀⠀⠀⠀⠖⣋⣡⣤⣸⡇⢻⣿⣿⣿⣿⣼⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⣿⣿⣧⠟⢁⣠⣄⡉⠹⠀⠀⠀⠀⠚⠉⢹⡉⠙⠻⣦⣿⣿⣯⣭⡿⢦⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⣿⣦⣮⣶⣷⣽⣤⠀⠀⠀⠀⣰⣯⣅⡙⢧⠀⢹⣿⣿⣿⣿⣇⠀⠹⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣋⣿⡇⠈⢻⣿⣿⠿⠁⠀⠀⠀⠀⠻⣿⣿⣿⣿⠁⠀⣾⣿⡆⣀⡌⢧⠀⠘⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣬⣹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⢰⣿⣿⣿⠙⡆⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⣽⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡟⣿⣿⡏⣡⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀Deobfuscated by Overpower
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡿⢳⡀⠀⠀⠀⠀⠐⢶⠀⠀⠀⠀⠀⠀⠀⣸⣿⡇⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Hisako Daddy⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠶⣿⣿⣇⣿⢻⣿⠀⠀⠀⠀          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠻⣿⣿⣿⣷⡙⠦⣤⡀⠀⢀⣠⡤⠖⠛⣡⣾⣿⣿⣿⣿⠈⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⢹⣿⢻⣿⣿⣦⣌⡉⠉⠉⢀⣀⣠⣾⣿⣿⣿⡏⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡏⠀⣹⣿⣿⣿⡏⠀⢸⣿⣿⣿⣿⣿⣯⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⡼⠁⡿⣿⣿⣧⣀⣜⣿⣿⡿⢟⣡⡞⠀⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⣸⣿⡿⢿⣴⣿⣿⣷⣶⣿⣿⣿⠁⠀⠀⠈⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⢀⣿⢷⣶⣿⠋⠙⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⣿⠹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⠀⠀⣼⣿⠸⣿⣧⣀⣴⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⣿⠀⠘⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠛⠀⣠⣾⣿⣿⡇⣿⣿⣿⣿⣿⡏⠀⠀⢹⠀⠀⠀⠀⢀⡇⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⢠⣾⣿⣿⣿⡿⣱⣿⣿⣿⣿⣿⠃⠉⠉⡟⠀⠀⠀⠀⢸⠁⠀⠀⣼⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⢰⣿⣿⣿⣿⣟⣵⣿⠿⢿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢸⠀⢀⡼⠁⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                             [UWU SPAMMER]
    """))
    print(Colorate.Diagonal(random_color_combination,"                   1. CUSTOM SPAM"))
    print(Colorate.Diagonal(random_color_combination,"                   2. SPAM HEARTS"))
    print(Colorate.Diagonal(random_color_combination,"                   3. SPAM FUCK"))
    print(Colorate.Diagonal(random_color_combination,"                   4. SPAM MOAI"))
    print(Colorate.Diagonal(random_color_combination,"                   5. SPAM SEX"))
    print(Colorate.Diagonal(random_color_combination,"                   6. SPAM NAZI"))
    print(Colorate.Diagonal(random_color_combination,"                   7. DELETE INBOX"))
    choice = input(Colorate.Diagonal(random_color_combination,"                   ~~> "))
    if choice == '1':
        custom_spam()
    if choice == '2':
        heart_spam()
    if choice == '3':
        fuck_spam()
    if choice == '4':
        curse_spam()
    if choice == '5':
        sex_spam()
    if choice == '6':
        nazi_spam()         
    if choice == '7':
        send_requests_with_given_and_random_username() 
if __name__ == "__main__":
    main()