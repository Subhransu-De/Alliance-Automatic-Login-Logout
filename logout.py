import requests
from time import sleep
from bs4 import BeautifulSoup
from dotenv import dotenv_values

config = dotenv_values(".env")


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


def main() -> None:
    try:
        logout = {'logout': 'Click here to logout'}
        requests.post(config['URL'].strip(), data=logout)
        sleep(10)
        pingStatus = []
        pingStatus.append(serverPing(config['PING_SERVER_FIRST']))
        pingStatus.append(serverPing(config['PING_SERVER_SECOND']))
        pingStatus.append(serverPing(config['PING_SERVER_THIRD']))
        finalPingResult = all(ping == False for ping in pingStatus)
        if finalPingResult:
            print("Something went wrong!")
        else:
            print("You Successfully Logged out! 🔒")
    except KeyboardInterrupt:
        print("Keyboard Interrupted Detected.")
    except:
        print("Something went wrong!")


if __name__ == '__main__':
    main()