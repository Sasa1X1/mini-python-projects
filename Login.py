from pystyle import *

print(Box.Lines("[+] LEARN PYTHON[+]"))
Write.Print("[+] This App For Login Page \n", Colors.red_to_blue,interval=0.1)
Write.Print("[+] write user name and password \n\n",Colors.blue_to_cyan,interval=0.1 )
print(Box.DoubleCube("exampl [1]"))

while True:
    username = Write.Input('write username: ', Colors.blue_to_green,interval=0.1)
    password = Write.Input('write pass: ', Colors.blue_to_green,interval=0.1)
    if username =='red' and password == '123456':
        Write.Print("[+] welcome admin \n",Colors.green,interval=0.1)
        input("\n press any key to exit: ")
    else:
        Write.Print('[+] Error again \n\n', Colors.red,intervapl=0.1)