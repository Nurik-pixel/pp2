# build-in functions


#1
def multiply_list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result
my_list = [1, 2, 3, 4]
print(multiply_list(my_list))

#2
import re
def calculateletters(text):
    lowercase = re.findall("[a-z]", text)
    uppercase = re.findall("[A-Z]", text)
    print(len(lowercase))
    print(len(uppercase))
text = "Text for task"
calculateletters(text)

#3
def is_palindrome(s):
    return s == s[::-1]
text = "madam"
print(is_palindrome(text))

#4
import math
import time

def delayed_square_root(value, delay_ms):
    time.sleep(delay_ms / 1000.0)
    result = math.sqrt(value)
    return result
number = 25100
delay_ms = 2123
result = delayed_square_root(number, delay_ms)
print(f"Square root of {number} after {delay_ms} milliseconds is {result:.12f}")


# dir-and-files


#1
import os
def list_contents(path="."):
    items = os.listdir(path)
    dirs = [i for i in items if os.path.isdir(os.path.join(path, i))]
    files = [i for i in items if os.path.isfile(os.path.join(path, i))]
    for d in dirs:
        print(f"  - {d}")
    for f in files:
        print(f"  - {f}")
    for i in items:
        print(f"  - {i}")
list_contents()
#2
import os
def check_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)
    print(f"Path: {path}")
    print(f"exists? {'Yes' if exists else 'No'}")
    print(f"Readable? {'Yes' if readable else 'No'}")
    print(f"Writeable? {'Yes' if writable else 'No'}")
    print(f"Executeable? {'Yes' if executable else 'No'}")

check_access("text.txt")
#3
import os
def check_path(path):
    if os.path.exists(path):
        print(f"Path: {path}")
        print(f"Directory: {os.path.dirname(path)}")
        print(f"File name: {os.path.basename(path)}")
    else:
        print("Path do not exist")
check_path("text.txt")
#4
def count_lines(file):
    try:
        with open(file, "r") as f:
            print(f"amount of line: {sum(1 for _ in f)}")
    except FileNotFoundError:
        print("File couldn't found")
count_lines("text.txt")
# 5
def write_list_to_file(file, data):
    try:
        with open(file, "w") as f:
            f.writelines("\n".join(data))
        print("List was written to file")
    except Exception as e:
        print(f"Error: {e}")
write_list_to_file("text.txt", ["Apple", "Pear", "Grape"])
# 6
import string
def create_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", "w") as f:
            f.write(f"This is {letter}.txt file\n")
    print("Files created")
create_files()
# 7
def copy_file(source, destination):
    try:
        with open(source, "r") as src, open(destination, "w") as dst:
            dst.write(src.read())
        print("File copied")
    except FileNotFoundError:
        print("Source file not found")
copy_file("source.txt", "destination.txt")
# 8
import os
def delete_file(file):
    if os.path.exists(file):
        os.remove(file)
        print("File deleted")
    else:
        print("File not found")
delete_file("text.txt")

