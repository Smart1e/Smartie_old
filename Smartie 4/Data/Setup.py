print('Hello User!\n Welcome to the Smartie installer.\nPlease ensure that you have followed the instructions in "Read Me Before Install.txt"')
import os
from time import sleep
from Installmods import install
import smartieJson as sj


print('I am about to open my file to import the modules necessary for me to work. All modules have been tested and scanned for any possible viruses by me AND the community.\nStarting in 3 seconds.')
sleep(1)
print('2')
sleep(1)
print('1')
sleep(1)
print('Commencing now. This may take a few minutes.')
install()
print('If you want to remove any of the modules, find the file called "Modules.txt" in the "Data" folder. after that just type the command:\n"pip uninstall modulename" to uninstall.')


if os.name == 'posix':
    #mac / linux
    system = '1'
else:
    #windows
    system = '2'


#https://opensource.com/article/19/7/save-and-load-data-python-json
#https://towardsdatascience.com/from-novice-to-expert-how-to-write-a-configuration-file-in-python-273e171a8eb3
print('Please enter your name here (this can be changed from the settings panel at any time')

user = str(input())

usepass = int(3)
while usepass != int(1) and usepass != int(2) and usepass != int(0):
    print('Do you want a password?')
    print('1 -- yes\n2 -- no')
    usepass = int(input())
    if usepass == int(1):
        passcode = str(input('Please enter password...  '))

    elif usepass == 0:
        usepass = 3
        
    elif usepass == int(2):
        usepass = int(0)
        passcode = int(0)

print('Finishing things up...')
sj.write({"system": system, "user": user, "passUsed": usepass, "password": passcode, "audio": "1", "mic": "1"})

print('Done')
sleep(1)
