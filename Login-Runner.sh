#!/bin/sh
#######################################
# Name:     Login-Runner.sh
# Purpose:  To Easily run login.py
# Revision: September 2021 - Initial version
#######################################

python login.py -u ${USERNAME:9}
read -t5 -n1 -r -p 'Exiting in the next five seconds...'