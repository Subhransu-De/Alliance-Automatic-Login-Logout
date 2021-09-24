import sys
from getpass import getpass
import ipaddress
import requests
from bs4 import BeautifulSoup
from dotenv import dotenv_values

config = dotenv_values(".env")


def isUserCredValid() -> bool:
    if config['USERNAME'] == '':
        print(len(sys.argv))
        if len(sys.argv) == 3 and sys.argv[1].lower() == '-u':
            config['USERNAME'] = sys.argv[2]
        else:
            config['USERNAME'] = input("Enter your Username : ")
    if config['PASSWORD'] == '':
        config['PASSWORD'] = getpass(prompt='Enter your Password : ',
                                     stream=None)

    if config['URL'] == '' or config['URL'] == 'http://xxx.xxx.xxx.xxx/0/up/':
        return False
    else:
        return True
    checkUrl = config['URL'].split('/')
    if checkUrl[0] == 'http:' and checkUrl[3] == '0' and checkUrl[4] == 'up':
        return True
    else:
        return False


def isAllianceUp() -> bool:
    try:
        checkAllianceCon = requests.get(config['URL'], timeout=30).status_code
        if checkAllianceCon == 200:
            return True
        else:
            return False
    except:
        return False


def allianceConnect() -> bool:
    try:
        soup = BeautifulSoup(
            requests.get(config['URL'], timeout=30).text, "html.parser")
        if soup.find(text=config['SERVER_OK_MESSAGE']
                     ) == config['SERVER_OK_MESSAGE']:
            return True

        userInfo = {
            'user': config['USERNAME'],
            'pass': config['PASSWORD'],
            'login': 'Login'
        }
        requests.post(config['URL'], data=userInfo)
        soup = BeautifulSoup(
            requests.get(config['URL'], timeout=30).text, "html.parser")
        return soup.find(
            text=config['SERVER_OK_MESSAGE']) == config['SERVER_OK_MESSAGE']
    except:
        return False


def serverPing(url: str) -> bool:
    print(f"Pinging \"{url}\"")
    try:
        checkCon = requests.get(config['URL'], timeout=30).status_code
        if checkCon == 200:
            return True
        else:
            return False
    except:
        return False


def getIp() -> list:
    try:
        soup = BeautifulSoup(
            requests.get(config['URL'] + 'llog').text, "html.parser")
        userIp = str(
            soup.select('table#mytable > tr:nth-child(2) > td:nth-child(2)')
            [0]).split('<td>')[1].split('</td>')[0]
        return isValidIpv4(userIp)
    except:
        return [False]


def isValidIpv4(userIp: str) -> list:
    try:
        ip = ipaddress.ip_address(userIp)
        return [ip, ip.version]
    except:
        return [False]


def main() -> None:
    try:
        if isUserCredValid():  # Step 1 : Check if Url Valid
            print("Checking if Alliance Server is UP... 🔍")
            if isAllianceUp():  # Step 2 : Check if Alliance Server Up
                print("Alliance Server is Up. Now Logging you in...")
                if allianceConnect(
                ):  # Step 3 : Logging user in Alliance Network
                    print("You are Logged in! ✅")
                    userIp = getIp()
                    if userIp[0] != False:
                        print(
                            f"Your IPv{userIp[1]} address is \033[92mxxx.xxx.xxx.xxx\033[0m."
                        )
                        # print(f"Your IPv{userIp[1]} address is \033[92m{userIp[0]}\033[0m.")
                    else:
                        print("Failed to retrive your Public IP!")
                    pingStatus = []
                    pingStatus.append(serverPing(config['PING_SERVER_FIRST'])
                                      )  # Step 4.1 : Ping First website
                    pingStatus.append(serverPing(config['PING_SERVER_SECOND'])
                                      )  # Step 4.2 : Ping Second website
                    pingStatus.append(serverPing(config['PING_SERVER_THIRD'])
                                      )  # Step 4.3 : Ping Third website
                    finalPingResult = all(ping == True for ping in pingStatus)
                    if finalPingResult:
                        print("Your Internet is working 🌐. Happy Browsing! 😀")
                    else:
                        print(
                            "Some or all ping test failed. It may be beacause of low Internet Speed. Please run a speedtest on \"https://www.speedtest.net/\""
                        )
                else:
                    print("Login failed! Check your USERNAME and PASSWORD.")
            else:
                print("Could not connect Alliance Server!")
        else:
            print(
                "The Url given in the .env file is not correct. The Url will be like this \"http://xxx.xxx.xxx.xxx/0/up/\""
            )
    except KeyboardInterrupt:
        print("Keyboard Interrupted Detected.")


if __name__ == '__main__':
    main()