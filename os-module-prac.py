import os
from datetime import datetime


print(os.getcwd())

os.chdir("C:\work\git")

print(os.getcwd())

print(os.listdir())

os.mkdir("test1") # only make 1 level directories
os.makedirs("test2/test1") # can make 1 or more level directories

# similarly for deleting there are 2 functions
os.rmdir("test1")
os.removedirs("test2/test1")

# os.rename("new_test.txt", "test.txt")

print(os.stat("test.txt").st_size, datetime.fromtimestamp(os.stat("test.txt").st_mtime))

print(os.walk(os.getcwd()))

print(os.environ.get("SPARK_HOME"))

new_path = os.path.join(os.environ.get("SPARK_HOME"), "test.txt")

print(new_path)

print(os.listdir())