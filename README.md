[Fundamentals Slideshow](https://docs.google.com/presentation/d/1TNYbdAjf5wTtpbe6MHHd0QciGDKF5Pa4I7TA_55u_pk/edit#slide=id.g1c24e327bd4_0_86)
[Dictionaries - Platform](https://login.codingdojo.com/m/506/12457/87306)
## Composite Type
### Dictionaries
#### Definition
An __unordered__ collection of __key-value pairs__ . **Not sequential in memory**
Each __KEY__ in a dictionary is unique
Mutable so can shrink or grow or be updated

**Dictionary Limitations:**
- Dictionaries are unordered, meaning the order of key-value pairs is not guaranteed in Python versions prior to 3.7.
- Keys must be hashable objects (immutable), which usually means they are strings, numbers, or tuples. Values can be of any data type.
- Dictionary operations can be slower than list operations for large datasets.
- Sequence operations/methods such as `slice()` or `append()` cannot be used with dictionaries

[Keys vs. Indexes](https://login.codingdojo.com/m/506/12457/87306)

|Keys|Indexes|
|---|---|
|Keys are typically strings|Indexes are always integers.|
|Keys are **_not_** in any sort of order, as dictionary values are NOT stored sequentially in memory.|Indexes are ordered (least to greatest) as list and tuple values are stored sequentially in memory.|
|Dictionaries **_ONLY_** have keys.|Dictionaries **_DO NOT_** have indexes.|

Python includes the following standalone functions for dictionaries:

- `len()` - give the total length of the dictionary.
- `str()` - produces a string representation of a dictionary.
- `type()` - returns the type of the passed variable. If passed variable is a dictionary, it will then return a `dict` type.
[Python dictionary DOCS](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
[Python dictionary methods DOCS](https://docs.python.org/3/library/stdtypes.html#typesmapping)
#### Syntax
Keys are typically string objects
bounded by`{}`
comma separated
colon separated key : value pairs
##### Create
```python
def create_dict():
	user = {"first_name" : "Cameron", "last_name" : "Smith", "age": 34 , "has_kids": True}
	other_user = {}
	# Multi-line Syntax
	user1 = {
    "first_name" : "Jane", 
    "last_name" : "Doe",
    "age" : 745,
    "has_kids" : True,
    'children' : ["bert", "ernie"]
    }
	  # print(user1)
	  return user1
this_user = create_dict()
```
##### Read
```python
print(user["first_name"])
```
You will use this 99.9% of the time
###### Checking for Key Existence
You can check if a key exists in a dictionary using the `in` operator.
```python
# if 'socialSecNum' not in user:
if "socialSecNum" in input_dict:
    print(input_dict["socialSecNum"])
else:
print("Not There")
```
__.get()__ will be handy if you want to *check a value of a dictionary but may not be there*
- will return None if it is not found
*None will evaluate to False in a conditional*
```python
print(input_dict.get('last_name'))
print(input_dict.get('socialSecNum'))

if input_dict.get('socialSecNum'):
    print(input_dict["socialSecNum"])
else:
print("Not There")
```
##### Add/Update
```python
other_user['first_name'] = "Ben"
```
__Nonsequential__ means that there is no `.append()`
By using the above syntax to add a value 
	*If the key already existed in the dictionary, then it will update its value*

`[ ]` is more straightforward and for consistency we will use almost exclusively
`.update()` it is used to update a dictionary with the key-value pairs from another dictionary or an iterable of key-value pairs
```python
dict1.update(dict2)

# , Nonsequential means that there is no `.append()`
# , var_location = value
this_user['first_name'] = "John"
print(this_user)
this_user.update({
"first_name" : "Jane",
"email" : "jd@email.com"
})
print(this_user,"\n")
```
`.update()` method merges the contents of the two dictionaries.
- If there were any common keys between the two dictionaries (in this case, `'first_name'` and `'last_name'`), the value from `dict2` overwrote the value in `dict1`.
- Unique keys from `dict2` are then added
##### Delete
`del` Removes the key and its associated value, returns nothing.
`.pop()` Removes the key and its associated value, returns the value
```python
del my_dict['email']  # Removes the key 'city' and its associated value
pop_return = my_dict.pop('age')  # Removes 'age' and returns its value
print(pop_return)
```
## Loops(dictionaries)
[Loops & Dictionaries - Platform](https://login.codingdojo.com/m/506/12457/90653)
### For In 
Access key name
```python
for each_key in user:
    print(each_key)
```
Then access value via key name
```python
for each_key in user:
    print(f"iterator: {each_key}")
    print(f"value: {my_dict[each_key]}")
```

Dictionaries also have methods that allow us to iterate through them and have the keys and/or values as the iterator.
Access key name `.keys()`
```python
for key in user.keys():
	print(key)
```
Access value `.values()`
```python
for val in user.values():
	print(val)
```
Access both `.items()`
```python
print(new_user.items())
for key, val in user.items():
	print(key, " = ", val)
```
`key` and `val` are just a simple iterator variable so...
```python
for rainbows, unicorn in other_user.items():
  print(rainbows, unicorn)
```
...still works

## [Python Dictionaries - DOCS](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
## [Dictionary Methods - DOCS](https://docs.python.org/3/library/stdtypes.html#dict)
## Nested Dictionaries & Lists
[Nested Dictionaries & Lists - Platform](https://login.codingdojo.com/m/506/12457/90576)
==use platform for conceptual review==
PSA: None of this is anything we haven't already covered. 
- It may *seem* complicated but its not. It is *complex*. 
- A complex thing is just a collection of simple things. 
- Be complex not complicated.
- ==review the Zen of Python==