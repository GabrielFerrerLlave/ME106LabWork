import serial
import matplotlib


for number in range(1,26):
    if number % 4 == 0:
        print(f"{number} is a multiple of 4!")
    else:
        print(number)

