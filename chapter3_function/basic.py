import random

def getAnswer(answer):
  if answer == 1:
    return "1"
  elif answer==2:
    return "2"
  elif answer==3:
    return "3"
  elif answer==4:
    return "4"
  elif answer==5:
    return "5"
  elif answer==6:
    return "6"
  elif answer==7:
    return "7"

r = random.randint(1,7)
num = getAnswer(r)
print(num)