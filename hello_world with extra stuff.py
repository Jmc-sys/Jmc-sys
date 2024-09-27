import time
a = 0
b = 0
c = 0

a = str('Hello')
b = str("World")
c = str("!")
# General purpose functions
print(a)  # Output to console
print(b,end="")  # Output to console
print(c)  # Output to consoleattached to previous line
print(len([a,b,c]))  # Get the length of a sequence
print(type("Hello"))  # Check the type of a variable
print(str(123))  # Convert to string
print(int("123"))  # Convert to integer
print(float("123.45"))  # Convert to float
print(range(5))  # Create a range of numbers
print(list("Hello"))  # Convert to list
time.sleep(2) # waits 2 seconds

# List manipulation
my_list = [3, 1, 4, 1, 5, 9, 2, 6]
print(my_list)
my_list.append(7)  # Add an item to the end
print(my_list)
print(my_list.sort())  # Sort the list in-place
print(my_list)
print(my_list.reverse())  # Reverse the list in-place
print(my_list.index(4))  # Find the index of an item
print(my_list.count(1))  # Count occurrences of an item
time.sleep(2) # waits 2 seconds

# Dictionary manipulation
my_dict = {"name": "Alice", "age": 30}
print(my_dict)
my_dict["city"] = "New York"  # Add a new key-value pair
print(my_dict)
print(my_dict.get("name"))  # Get the value of a key, or None if not found
print(my_dict.keys())  # Get all keys
print(my_dict.values())  # Get all values
print(my_dict.items())  # Get all key-value pairs as tuples
time.sleep(2) # waits 2 seconds

# String manipulation
my_string = "Hello, world!"
print(my_string)
print(my_string.upper())  # Convert to uppercase
print(my_string.lower())  # Convert to lowercase
print(my_string.split(","))  # Split string into a list
print(my_string.replace("Hello", "Hi"))  # Replace a substring
print(print(my_string),'starts with "Hello"?')
print(my_string.startswith("Hello"))  # Check if string starts with a substring
print(print(my_string),'ends with "world!"?')
print(my_string.endswith("world!"))  # Check if string ends with a substring
time.sleep(2) # waits 2 seconds
