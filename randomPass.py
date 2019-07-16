import string
from random import *
import pyautogui
from time import *
import subprocess



allchar = string.ascii_letters + string.digits

while True:
    try:
        number = int(input("Enter # of random password you need: "))
        min_char = int(input("Enter minimum digit: "))
        max_char = int(input("Enter maximum digits: "))
        if number > 0 and min_char > 0 and max_char > 0:
            break
        else:
            print("Amount can't be negative or zero, try again")

    except ValueError:
        print("Sorry that is not valid number. Type again.")


#subprocess.call(['C:\WINDOWS\system32\\notepad.exe'])

pyautogui.hotkey('win','r')
pyautogui.typewrite('notepad')
pyautogui.press('enter')
sleep(2)
pyautogui.typewrite('Now printing your '+str(number)+" random password(s)")
pyautogui.press('enter')
pyautogui.press('enter')

y = 1



for x in range(number):
    password = ("".join(choice(allchar) for x in range(randint(min_char, max_char))))
    pyautogui.typewrite("Random password #"+str(y)+": " + password)
    y += 1
    pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.typewrite("There you go! Glad to help!")
y = 1
with open("randomPasswords.txt", "w+") as randompass:
    for x in range(number):
        password = ("".join(choice(allchar) for x in range(randint(min_char, max_char))))
        l = ["Passwords #"+str(y)+": " + password + "\n"]
        randompass.writelines(l)
        y += 1



randompass.close()




