#!/usr/bin/python3
import json

# Just mucking around and modifying code from w3schools, but this is actually kind of useful and fun.  Yay!

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# a Python object (dict):
z = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
a = json.dumps(z)

# the result is a JSON string:
print(a)

# so I can convert from dicts, to jason and back again in python fairly easily.  That's good to know.
# much aws automation goo is available in jason so this may be useful depending.
