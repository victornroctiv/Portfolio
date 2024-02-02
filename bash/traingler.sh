#!/bin/bash
#Input 3 different lengths to see what kind of Triangle it is.(Equilateral, Isosceles, or Scalene)

echo "Please Input 3 different values"
read x; read y; read z

if (( x >= 1000 || y >= 1000 || z >= 1000 || x == 0 || y == 0 || z == 0)) 
    then echo "out of range"
        exit
fi

if (( x + y <= z || y + z <= x || z + x <= y ))
    then echo "not a triangle"
        exit
fi

if (( x == y && y == z ))
    then echo "equilateral"
elif (( x == y || y == z || z == x ))
    then echo "isosceles"
else
    echo "scalene"
fi
