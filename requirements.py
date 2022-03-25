# only for Debian Users right now
import os
print("This Script Would Need acpi as to know battery status!")
var = input("Do You Want to Allow ?\nif yes then please input root password to install (y/n): ")
if(var=='y'or var=='Y'):
    os.system('sudo apt install acpi')