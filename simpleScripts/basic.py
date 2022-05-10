## math
import json
import math

5 / 3
5 // 3 # rounds

#bool
True
not True # equals to "!"
True + True # 2
True * 8 # 8
bool(5) # casting int to boolean

# && === and
# || === or
1 and 0 # false
1 or 0 # true

a = [1,2,3,4]
b = a
a is b # checks if both refer to the same object

## strings
name = 'Hitoshura'
"a" + "b" # concat
"a" "b" # also concats
"abc"[0] # a, since strings are also array of chars
len("abcd") # 4
f"she said {name}" # format
f"{name} has {len(name)} chars in her name"

# none == object
bool(0) #false
bool("") #false
bool([]) #false
bool({}) #false
bool(()) #false

# I/O
print("aye")
var_iable = input("give input: ")

## ""ternary""
"aye" if 0 > 1 else "nay"

## lists
li = [1,2,3]
li.append(2)
li.pop()
li[0] # access list data just like array data
li[-1] # last element of the list

# li[start:end:step]
li[1:3] # index 1 until 3
li[2:] # show all starting at index 2
li[:3] # start from 0 and stop at 3
li[::2] # show every second entry
li[::-1] # show in reverse order

o_li = [4,5,6]
del li[2] # rm specific elementS of a list
li.remove[2] # rm the first occurence of a value
li.insert(1,2) # insert element at specific index
li + o_li # fuse lists without modifing their values
li.extend(o_li) # elements of o_li fused with elements of li

1 in li # checks if the value is in the list
len(li)

## tuples
# same as lists, but immutable
tup = (1,2,3)
type((1)) # int
type(()) # tuple
type((1,)) # tuple

# lists and tuple can be unpacked into variables
a, b, c = (1, 2, 3) # a=1, b=2, c=3

## dictionaries
e = {"o": 1, "b": 2, "c": 3}
e["o"] # => 1
e.keys() # => o, b, c
e.values() # => 1, 2, 3
"o" in e # => true
e.get("o") # => 1
e.get("asd") # => none
# adding to tuple
e.setdefault("d", 4)
e.update({"e", 4})
del e["e"]

s_var = 1
## conditionals
if s_var > 10:
  print("bigger")
elif s_var < 10:
  print("smaller")
else: 
  print("equal")

## loops
for animal in ["dog", "cat", "mouse"]:
  print("{} is a mammal".format(animal)) # .format is used to interpolate strings

# range: iterables from 0 to the specified number
for i in range(4):
  print(i)

# range(start, end)
for i in range(4,8):
  print(i)

# range(start, end, step)
for i in range(4,20,2):
  print(i)

# prints both index and value when interating through a list
animals = ["dog", "cat", "mouse"]
for i,value in enumerate(animals):
  print(i, value)

x = 0
while x < 4:
  print(x)
  x += 1

try:
  raise IndexError("error thrown")
except IndexError as e:
  pass
except (TypeError, NameError):
  pass
else:
  print("daijobu")
finally:
  print("clean up here")

with open('mFile.txt') as f:
  for line in f:
    print(line)

## w+r to file
content = {"aa": 12, "bb": 21}
with open("mFile.txt", "w+") as file:
  file.write(str(content)) # writes string

with open("nFile.txt", "w+") as file:
  file.write(json.dump(content))

with open('mFile.txt', "r+") as file:
  content = file.read()
print(content)

with open('nFile.txt', "r+") as file:
  content = json.load(file)
print(content)


## functions
def add(x,y):
  print("x is {}, y is {}".format(x,y))
  return x + y
add(2,3)

def swap(x,y):
  return y, x # the return is a tuple

global aGlobal
aGlobal = 2

(lambda x: x > 2)(3)

from math import ceil, floor # import specific functions only
import math as m # import functions with abreviations

math.sqrt(2) == m.sqrt(2)
print(ceil(3.7))
print(floor(3.7))

dir(m) # show attributes and derived items