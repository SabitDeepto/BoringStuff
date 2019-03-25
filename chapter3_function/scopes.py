''' কোন ফাংশনের লোকাল স্কোপ এ থাকা ভেরিয়েবল অন্য ফাংশনের লোকাল স্কোপে কখনোই  ব্যবহার করা যায় না । 
ভেরিয়েবল কে গ্লোবাল করে দিলে ফাংশন ইন্সট্যানশিয়েট করে তখন ই উক্ত লোকাল ভেরিয়েবল ব্যবহারকরা যাবে ।
ফাংশন ইন্সট্যানশিয়েট করে যদি একই নামে অন্য ভেরি তৈরি করা হয় তখন অন্যাটা কাজ করবে ।

def spam():
    global egg_from
    egg_from = "chicken"


def bacon():
  spam()
  print(egg_from)

bacon()
 
''' 

# local scope can't use var from another local scope
def spam():
  egg = 99
  bacon()
  print(egg)
  print(ham)

def bacon():
  ham =1221
  egg = 0

spam()

# Global vars can be read from local scope
def spam():
  print(egg)
egg = 23

spam()

# Global and Local with same Name
def spam():
  egg = "spam local"
  print(egg)

def bacon():
  egg = "bacon local"
  print(egg)
  spam()
  print(egg)

egg = 'global'
bacon()

# Guess the number game
import random
secretNumber = random.randint(1, 9)

for number in range(1,9):
  print("enter a number")
  num = int(input())

  if num > secretNumber:
    print("too high")
  elif num < secretNumber:
    print("to0 low")
  else:
    print("perfect ! ", f"the secret number was also {secretNumber}")
    break
    print(secretNumber)
