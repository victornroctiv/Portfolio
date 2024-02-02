#!/bin/bash

echo "Drop me a domain name of sorts"
read doman_name
function giveinfo(){
    echo "---- who is"
    'whois' $doman_name
    echo "---- dig"
    'dig' $doman_name
    echo "---- host"
    'host' $doman_name
    echo "---- nslookup"
    'nslookup' $doman_name
}
giveinfo > DomainNameInfo.txt
echo "Info Dropped into a DomainNameInfo Text File"