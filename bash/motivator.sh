#!/bin/bash

echo "How are you doing today?(enter Good, Bad, Okay, or Not great)"
read response

echo "$response!?"

case $response in
    
    Good | good)
        echo "Amazing! lets keep the momentum going and conquer the day!"
        ;;
    
    Bad | bad)
        echo "Oh I see, it's okay to have bad days, I'll be here for and with you regardless!"
        ;;
        
    Okay | okay | meh | Meh)
        echo "Sweet, just an average day huh? Welp, make sure your drinking water and resting when you need to."
        ;;
    *)
        echo "What'd you say? My programmer didnt add a response for that...fortunately."
        ;;
esac
