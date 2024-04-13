from pystyle import *

print(Box.Lines("[+] LEARN PYTHON[+]"))
Write.Print("[+] This App For CalC \n", Colors.red_to_blue,interval=0.1)
print(Box.DoubleCube("exampl [2]"))

while True:
    number1 = int(Write.Input("[+] write first number: ",Colors.blue_to_green,interval=0.1))
    operator = Write.Input("write math code: ",Colors.orange,interval=0.1)
    number2 = int(Write.Input('[+] write the seconde number:', Colors.blue_to_green,interval=0.1))
    if operator == "+":
        Write.Print('[+] The Result Is: ',Colors.green,interval=0.1)
        print(number1+number2)
        break

    elif operator == "-":
        Write.Print('[+] The Result Is: ',Colors.green,interval=0.1)
        print(number1-number2)
        break

    elif operator == "*":
        Write.Print('[+] The Result Is: ',Colors.green,interval=0.1)
        print(number1*number2)
        break

    elif operator == "/":
        Write.Print('[+] The Result Is: ',Colors.green,interval=0.1)
        print(number1/number2)
        break
    else:
        Write.Print("\n [-] please write - (+ or - or / or *) \n",Colors.red,interval=0.1)