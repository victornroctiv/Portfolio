#!/bin/bash

user=x
while [ $user = x ]
do
echo "Please make a selection"
echo "1 To print Hello World!" 
echo "2 To Show Network Config"
echo "3 For Pinging Options"
read input
    if [ $input = 1 ]
        then echo "Hello World!"
    elif [ $input = 2 ]
        then ifconfig
    elif [ $input = 3 ]
        then 
            echo "Enter: 1 to ping an IP | 2 to ping a website"
            read that
            if [ $that = 1 ]
                then
                    echo "Enter an IP Address"
                    read address
                    ping -c 1 $address
            elif [ $that = 2 ]
                then
                    echo "Enter a website"
                    read website
                    ping -c 1 $website
            else echo "Access Denied"
            fi
    else echo "Invalid entry"
fi
echo "Do you want to do something else? x = Yes | o = no"
read user
done
echo "Your call boss."