# Alliance Automatic Login & Logout

Python script to automatically log in and log out of Alliance Account.

## What's included?
* Python Script for Login
* Logout Python Script
* Shell Script file for Login ([Linux](https://en.wikipedia.org/wiki/Linux) based system)
* Shell Script file for Logout ([Linux](https://en.wikipedia.org/wiki/Linux) based system)
* DOS Batch file for Login ([Windows NT](https://en.wikipedia.org/wiki/Windows_NT))
* DOS Batch file for Logout ([Windows NT](https://en.wikipedia.org/wiki/Windows_NT))
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to packages in requirements.txt
```
$ pip install -r requirements.txt
```
## Usage
User can log in two different ways. First run the command below.
```
$ cp .env.example .env
```
```
...
URL=http://xxx.xxx.xxx.xxx/0/up/
...
```
Enter the Alliance login IP in the .env file.
### First Option (Recommended)
###### Give the username from command line and password will be taken by the script using [getpass](https://docs.python.org/3/library/getpass.html)
```
$ python login.py -u YOUR-USERNAME
```
User can also store their username in .env file and then run the python script.
```
USERNAME=YOUR-USERNAME
...
```
```
$ python login.py
```
In this case user will be logged in without providing their username everytime but password will be asked everytime.
### Second Option
###### Store the username and password in .env file.
Now enter your username and password in .env file.
```
USERNAME=YOUR-USERNAME
PASSWORD=YOUR-PASSWORD
...
```
```
$ python login.py
```
In this case username and password is never asked by the python script. Although this option is **Not Recommended** as password is physically stored in the disk.\
Login-Runner.bat and Login-Runner.sh can be used.
___
**To Log Out**
```
$ python logout.py
```
Logout-Runner.bat and Logut-Runner.sh can be used.
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)