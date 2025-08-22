#write a lambda / anonymous function to check number is palindron
isPalindron = lambda numOne : True if numOne == numOne[::-1] else False
print(isPalindron("1"))

