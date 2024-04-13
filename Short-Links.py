from pystyle import *
import pyshorteners as short

print(Box.Lines("[+] LEARN PYTHON[+]"))
Write.Print("[+] This App For Short Urls \n", Colors.red_to_blue, interval=0.1)
print(Box.DoubleCube("exampl [3]"))

url = Write.Input("[+] write url for shortening: ", Colors.blue_to_green, interval=0.1)
sh = short.Shortener()
short_url = sh.tinyurl.short(url)
Write.Print(f"[+] Shortened URL: {short_url}\n", Colors.green, interval=0.1)
input("Press any key to exit...")
