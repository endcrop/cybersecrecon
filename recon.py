import os
import time
print("Kali Linux ip Recon Tool")
time.sleep(1)
print("!!! to use proxychains make sure you have them configured in /etc/proxychains4.conf !!!")
time.sleep(1)
# nmap function
def nmap():
    ip = input("target ip: ")
    proxy = input("would you like to use proxychains?\ny/n: ")
    if proxy == "y":
         os.system(f"proxychains4 nmap {ip} -Pn")
         print("\n scan complete")
         time.sleep(3)
         return
    elif proxy == "n":
        os.system(f"nmap {ip} -Pn")
        print("\n scan complete")
        time.sleep(3)
        return
    else:
        print("please enter a valid input!")
        time.sleep(3)
        return
#ping function
def ping():
    ip = input("target ip: ")
    proxy = input("would you like to use proxychains?\ny/n: ")
    if proxy == "y":
        os.system(f"proxychains4 ping -c 4 {ip}")
        print("\npings completed")
        time.sleep(2)
        return
    elif proxy == "n":
        os.system(f"ping -c 4 {ip}")
        print("\npings completed")
        time.sleep(2)
        return
    else:
        print("please enter a valid! ")
        time.sleep(3)
        return
#wireshark function
def wireshark():
    usr = input("are you sure you would like to open wireshark?\ny/n: ")
    if usr == "y":
        os.system("cd")
        os.system("wireshark")
    elif usr == "n":
        return
    else:
        print("please enter a valid input")
#burpsuite function
def burp():
    usr = input("are you sure you want to open burpsuite?\ny/n: ")
    if usr == "y":
        proxy = input("would you like to use proxychains?\ny/n: ")
        if proxy == "y":
            os.system("proxychains4 burpsuite")
        elif proxy == "n":
            os.system("burpsuite")
        else:
            print("please enter a valid input!")
            time.sleep(3)
            return

#gets user input for which choice

on = "5"
while on == "5":
    choice = input("1. nmap scan\n2. ping ip\n3. open wireshark\n4. burpsuite\n: ")
    if choice == "1":
        nmap()
    elif choice == "2":
        ping()
    elif choice == "3":
        wireshark()
    elif choice == "4":
        burp()
    else:
        print("enter a valid input twin")