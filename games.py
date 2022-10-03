import os,sys,time,os,json,requests,re
from colorama import Fore,Back,init

def autoketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.005)

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW

# Buat Ip/Tanggal
ip=requests.get('https://api.ipify.org').text
localtime=time.asctime(time.localtime(time.time()))

Hijau="\033[1;92m "
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
merah="\033[1;91m"
biru="\033[1;96m"

# Jamgan Di Ganti
def game():
    os.system("pkg install nsnake")
    os.system("pkg install bastet")
    os.system("pkg install greed")
    os.system("pkg install ninvaders")

# Kalo Mau Di Ganti Bilang Gua Anj
def banner():
    autoketik (f"""
{biru}╔╦╗{W}┌─┐┬─┐┌┬┐┬ ┬─┐ ┬   {R}╔═╗{Y}┌─┐┌┬┐{G}┌─┐┌─┐
{biru} ║ {W}├┤ ├┬┘││││ │┌┴┬┘───{R}║ ╦{Y}├─┤│││{G}├┤ └─┐
{biru} ╩ {W}└─┘┴└─┴ ┴└─┘┴ └─   {R}╚═╝{Y}┴ ┴┴ ┴{G}└─┘└─┘
{abu}--------------------------------------
      {putih}[{biru}•{putih}] {biru}Author {putih}: SanzzXD
      {putih}[{biru}•{putih}] {biru}Youtube {putih}: SanzzXD

      {W}[{Y}•{W}] Ip Lu Nih Njing{R}:{Y} {ip}
      {W}[{Y}•{W}] Waktu/Jam{R}:{Y} {localtime}
""")

# Jangan Di Ganti, Ntar Eror
os.system("clear")
def banner2():
    print(f"""
{W}[{biru}1{W}] {W}Games Snake {W}({G}On{W})
{W}[{biru}2{W}] {W}Games Bastet {W}({G}On{W})
{W}[{biru}3{W}] {W}Games Greed {W}({G}On{W})
{W}[{biru}4{W}] {W}Games Ninvaders {W}({G}On{W})
{W}[{biru}5{W}] {W}Follow IG Gua Ngab {W}({G}On{W})
""")

def start():
    banner()
    banner2()
    pil=input(f"  Pilih No  : ")
    if pil == "1":
        game()
        os.system("nsnake")
    if pil == "2":
        game()
        os.system("bastet")
    if pil == "3":
        game()
        os.system("greed")
    if pil == "4":
        game()
        os.system("ninvaders")
    if pil == "5":
        os.system("xdg-open https://instagram.com/eabdalmufid_")

start()
