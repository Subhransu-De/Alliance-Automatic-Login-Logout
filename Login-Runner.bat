:: Name:     Login-Runner.bat
:: Purpose:  To Easily run login.py
:: Revision: September 2021 - Initial version

@ECHO OFF
set /p USERNAME=<.env
python login.py -u %USERNAME:~9%
ECHO Exiting in the next five seconds...
timeout 5