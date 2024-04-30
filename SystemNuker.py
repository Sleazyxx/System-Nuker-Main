import colorama
from colorama import Fore
import os
import subprocess
from pystyle import *
import time

def load_proxies():
    print("❗Loading proxies❗")
    for i in range(20):
        time.sleep(0.1)
        print("=", end='', flush=True)
    time.sleep(1)
    print("\n❗Proxies loaded successfully❗")
    print("\n=====================")
    time.sleep(0.5)
    print("❗Activating proxies❗")
    for i in range(20):
        time.sleep(0.1)
        print("=", end='', flush=True)
    time.sleep(1)
    print("\n🟢Proxies activated🟢")
    time.sleep(0.5)

with open('utilities/Tools/proxies.txt') as f:
    proxies = f.readlines()
    
load_proxies()
class Colors:
    purple_to_blue = Fore.WHITE + Fore.LIGHTBLACK_EX
    blue_to_purple = Fore.LIGHTBLACK_EX + Fore.WHITE
    purple = Fore.WHITE
    reset = Fore.RESET
    light_red = Fore.LIGHTBLACK_EX

class Write:
    @staticmethod
    def Print(text, color, interval):
        print(color + text, end='', flush=True)

def print_menu():
    colorama.init()
    m = Colors.purple
    w = Colors.reset
    b = Colors.blue_to_purple
    lr = Colors.light_red

    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar pantalla
    print('')
    print('')
    Write.Print("""      ███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗    ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ \n""", Colors.purple_to_blue, interval=0.000)
    Write.Print("""      ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗\n""", Colors.purple_to_blue, interval=0.000)
    Write.Print("""      ███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║    ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝\n""", Colors.purple_to_blue, interval=0.000)
    Write.Print("""      ╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║    ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗\n""", Colors.purple_to_blue, interval=0.000)
    Write.Print("""      ███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║    ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║\n""", Colors.purple_to_blue, interval=0.000)
    Write.Print("""      ╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝\n""", Colors.purple_to_blue, interval=0.000)
    Write.Print("      ════════════════════════════════════════════════════════════════════════════════════════════════\n", Colors.purple_to_blue, interval=0.000)
    print(f'''{m}'''.replace('$', f'{m}${w}') + f'''
           {m}[{w}1{Fore.RESET}{m}]{Fore.RESET} DOSAttack        |{Fore.RESET}{m}[{w}2{Fore.RESET}{m}]{Fore.RESET} FN IPsniffer       |{Fore.RESET}{m}[{w}3{Fore.RESET}{m}]{Fore.RESET} GcSpammer{Fore.RESET}
           {m}[{w}4{Fore.RESET}{m}]{Fore.RESET} Gmail BruteForce |{Fore.RESET}{m}[{w}5{Fore.RESET}{m}]{Fore.RESET} ImageLogger        |{Fore.RESET}{Fore.RESET}{m}[{w}6{Fore.RESET}{m}]{Fore.RESET} Login Bruteforce{Fore.RESET}
           {m}[{w}7{Fore.RESET}{m}]{Fore.RESET} Massreport       |{Fore.RESET}{m}[{w}8{Fore.RESET}{m}]{Fore.RESET} TokenbruteForce    |{Fore.RESET}{m}[{w}9{Fore.RESET}{m}]{Fore.RESET} TokenDecrypt{Fore.RESET}
           {m}[{w}10{Fore.RESET}{m}]{Fore.RESET} UsernameScrape  |{Fore.RESET}{m}[{w}11{Fore.RESET}{m}]{Fore.RESET} WebhookDestoryer  |{Fore.RESET}{m}[{w}0{Fore.RESET}{m}]{Fore.RESET} Exit{Fore.RESET}''')
    print('')
    Write.Print("      ═══════════════════════════════════════════════════════════════════════", Colors.purple_to_blue, interval=0.000)

def execute_script(script_name):
    if script_name:
        script_path = os.path.join('utilities', 'Tools', script_name)
        subprocess.run(['python', script_path], shell=True)

if __name__ == "__main__":
    while True:
        print_menu()
        choice = input(f'{Colors.purple}[{Colors.reset}>{Colors.purple}]{Colors.reset} Choice?: ')
        if choice.isdigit() and int(choice) in range(12):
            script_name = {
                '1': 'DOSAttack.py',
                '2': 'FN IPsniffer.py',
                '3': 'GcSpammer.py',
                '4': 'Gmail BruteForce.py',
                '5': 'ImageLogger.py',
                '6': 'Login Bruteforce.py',
                '7': 'Massreport.py',
                '8': 'TokenbruteForce.py',
                '9': 'TokenDecrypt.py',
                '10': 'UsernameScrape.py',
                '11': 'WebhookDestoryer.py',
                '0': None
            }.get(choice)
            if script_name:
                execute_script(script_name)
            else:
                if choice == "0":
                    exit_choice = input(f"\n[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Are You Sure You Want To Exit? Y/N: ").lower()
                    if exit_choice == "y":
                        break
                    elif exit_choice == "n":
                        continue
                    else:
                        print("Invalid choice.")
                else:
                    print("Invalid choice.")
        else:
            print("Invalid choice.")
