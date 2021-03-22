import random
import time

charTypes = ['digit', 'letter', 'symbol']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '?', '$', '&', '#', '%', '*']

def getChar():
  charType = random.choice(charTypes)
  if charType == 'digit':
    char = random.choice(digits)
  elif charType == 'letter':
    char = random.choice(letters)
  elif charType == 'symbol':
    char = random.choice(symbols)
  return char
  
char1 = getChar()
char2 = getChar()
char3 = getChar()
char4 = getChar()
char5 = getChar()
char6 = getChar()
char7 = getChar()
char8 = getChar()
char9 = getChar()
char10 = getChar()
char11 = getChar()
char12 = getChar()
char13 = getChar()
char14 = getChar()
char15 = getChar()
char16 = getChar()
char17 = getChar()
char18 = getChar()
char19 = getChar()
char20 = getChar()
char21 = getChar()
char22 = getChar()
char23 = getChar()
char24 = getChar()
char25 = getChar()

result = char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8 + char9 + char10 + char11 + char12 + char13 + char14 + char15 + char16 + char17 + char18 + char19 + char20 + char21 + char22 + char23 + char24 + char25

print('WARNING: The generated password is NOT easy to remember! It is recommended that you save it somewhere safe.')
print('Your generated password is: ' + result)
time.sleep(999)