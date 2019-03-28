# try except
try:
  spam = ['cat', 'bat', 'rat', 'elephant']
  x = spam[23]
  print(x)
except IndexError:
  print("An exception occurred") 

""" প্রথম ইনডেক্স >  শো করে লিস্টের কোন ইনডেক্সে আমি এক্সেস নিবো ,
দ্বিতীয় ইনডেক্স >  কত তম ইনডেক্সের ভ্যালু চাই সেইটার জন্য দায়ী । 
spam[1][2] --> [1] দ্বিতীয় লিস্ট [২] দুই নাম্বার ইনডেক্স 
output: 30"""

spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam[1][2])

# Delete index
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[1]
spam.remove("bat")

# append index
spam.append("apple") #added to the last index
spam.insert(1, "orange")

# loop
name = 'Zophie'
for i in name:
    print(f'*********{i}**********')

*********Z**********
*********o**********
*********p**********
*********h**********
*********i**********
*********e**********

# tuple
''' 
append() or extend() || remove() or pop() || insert , del 
- বলে টাপলে কিছু নাই ।  যখন রাইট প্রটেক্টেড অনেক গুলা ভ্যালূ কোথাও স্টোর করতে চাই তখন ই টাপল ব্যবহার করবো । 

'''
