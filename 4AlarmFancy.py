import serial
import matplotlib

nth = ["first", "second", "third", "fourth", "fifth","sixth"]
i = 0
for number in range(1,26):
    if (number % 4 == 0):
        print(f"{number} is the {nth[i]} multiple of 4!")
        i += 1
    else:
        print(number)
    
        

