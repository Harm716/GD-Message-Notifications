import requests, base64, time
from os import system, name
from json import loads
from itertools import cycle
from win10toast import ToastNotifier
from urllib.request import urlretrieve

to = ToastNotifier()

def xor(data, key):
	return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(data, cycle(key)))

def gjp(data):
	return base64.b64encode(xor(data,"37526").encode()).decode()

username = input("Enter username: ")

password = input("Enter password: ")

dur = input("How often you want to be notified (in seconds): ")

if name == "nt":
    system('cls')
else:
    system('clear')

accountID = loads(requests.get(f"http://gdbrowser.com/api/profile/{username}").text)['accountID']

urlretrieve("http://www.filehosting.org/file/download/915111/y3DlqIe0BCMzEmzW","gd.ico")

secret = "Wmfd2893gb7"

def getUnreads(accountID,password):
    pl = {
        'accountID': accountID,
        'gjp': gjp(password),
        'targetAccountID': accountID,
        'secret': secret
    }
    return requests.post("http://boomlings.com/database/getGJUserInfo20.php",pl).text.split("::")[3].split(":")[3]

while 1:
    unreads = getUnreads(accountID,password)
    try:
        if (unreads != 0):
            to.show_toast("Geometry Dash",f"You've got mail!\n{unreads} unreads messages in your inbox!",icon_path="gd.ico",duration=5,)
        else:
            print("No new messages in your inbox.")
    except:
        print("Error fetching message count.")
    time.sleep(int(dur))