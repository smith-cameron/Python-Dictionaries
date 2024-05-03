
# _ Dictionaries
# < An unordered collection of key-value pairs . 
""" bounded by {}
    keys are typically strings
    an item = colon separated key : value
    comma separated pairs of items
"""
  # > {"key":value, "key":value, ...}
# < Not sequential in memory (NO INDEX)
# < Each KEY in a dictionary is unique
# < Mutable so can shrink or grow or be updated
# < METHODS
  # > https://docs.python.org/3/library/stdtypes.html#typesmapping

# < Create Read Update Delete
# > Create
def create_dict():
  user = {"first_name": "Liam", "last_name": "Brown", "age": 538, "has_kids":False}
  user2 = {}
  user3 = {
    "first_name": "Liam", 
    "last_name": "Brown", 
    "age": 5,
    "has_kids":False
  }
  # print(user , "\n")
  return user
this_user = create_dict()

# > Read
def read_dict_values(input_dict):
  print(input_dict["age"])
  if "socialSecNum" in input_dict:
    print(input_dict["socialSecNum"])
  else:
    print("NOT FOUND")

  print(input_dict.get("first_name"))
  print(input_dict.get("socialSecNum"))

  if input_dict.get("last_name"):
    print(input_dict["last_name"])
  else:
    print("NOT FOUND")

# read_dict_values(this_user)

# > Update/(ADD)
def update_dict(this_user):
  # , Nonsequential means that there is no `.append()`
  # , var_location = value
  this_user["first_name"] = 'James'
  this_user["email"] = "jb@email.com"
  updated_data = {
    "first_name": "Liam", 
    "email": "lb@email.com", 
    "age": 45,
    "has_kids":True,
    "children": ["cheddar", "pumpkin"]
  }
  this_user.update(updated_data)
  return this_user

new_user = update_dict(this_user)
# print(new_user)

# > Delete
def remove_values(input):
  print(input)
  del input['age']
  print(input)
  pop_return = input.pop('email')
  print(pop_return)
  print(input)
# remove_values(new_user)

# < Dictionaries and Loops
# > By Key
def by_key(new_user):
  for unicorn in new_user:
    print(unicorn)
# by_key(new_user)

# > By Value Via Key
def value_by_key(new_user):
  for unicorn in new_user:
    print(new_user[unicorn])
# value_by_key(new_user)

# > .keys()
def keys_built_in(new_user):
  for key in new_user.keys():
    print(key)
# keys_built_in(new_user)

# > .values()
def values_built_in(new_user):
  for val in new_user.values():
    print(val)
# values_built_in(new_user)

# > .items()
def items_built_in(new_user):
  print(new_user.items())
  for key, val in new_user.items():
    print(key, val)
# items_built_in(new_user)

#  < Practice
# ? Create a function that creates a user dictionary...
# ? Add each dictionary to a list
all_users = []
def create_user(f_name, l_name, age, email, has_kids = False):
  user = {
    "first_name": f_name, 
    "last_name": l_name, 
    "age": age,
    "email": email,
    "has_kids": has_kids,
    "children" :[]
  }
  all_users.append(user)
  return user

user_timmy = create_user("Timmy", "Jimmy-Jam", 33, "tjj@email.com")
create_user("Ben", "Jammin", 43, "bj@email.com")
create_user("Clint", "Eastwood", 399, "ce@email.com", True)
create_user("Liam","Brown", 538, "lb@email.com", has_kids = True)
create_user("DB", "Cooper", 90, "db@email.com")
create_user("Kaya", "Seawalker", 26, "ks@email.com")

# ? Create a function that searches for a user and update children
def find_one(users, fname_to_find, new_values):
  # print(users)
  for user in users:
    print(user)
    # if user matches the key we are looking for that is the one we want to update
    if user.get("first_name") == fname_to_find:
      # print("found it!")
      # define values to update
      new_data = {
        "children": new_values
      }
      # use .update() to pass children names to user
      user.update(new_data)
      user.update()
find_one(all_users, "Liam", ["cheddar", "pumpkin", user_timmy])