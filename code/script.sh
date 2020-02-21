#!/bin/bash

read -p "Enter two numbers: " var1 var2

read -p "Would you like to add, subtract, divide, or multiply? " sign1

case $sign1 in

	add)
		echo "Adding..."
		product=$((var1+var2))
		;;
	subtract)
		echo "Subtracting..."
		product=$((var1-var2))
		;;
	divide)
		echo "Dividing..."
		product=$((var1/var2))
		remainder=$((var1%var2))
		if [ $product -eq 0 ]
		then
			echo "$var1 does not divide into $var2"
			exit 1
		else
			echo "$var1 divides into $var2 $product times with a remainder of $remainder"
			exit 1
		fi
		;;
	multiply)
		echo "Multiplying..."
		product=$((var1*var2))
		;;
	*)
		echo "That i'snt an option"
		exit 1
		;;
esac

echo "The value is $product"
