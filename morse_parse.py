from time import sleep

message = "000020201002010021112011211120102010021002101011"

# 0 = . , 1 = _ , 2 = letter separator

def long_beep():
  print("beeeeeeep")
  sleep(0.4)

def beep():
  print("beep")
  sleep(0.2)

def space():
  print("--")

for letter in message:
  if letter == "0":
    beep()
  elif letter == "1":
    long_beep()
  else:
    space()