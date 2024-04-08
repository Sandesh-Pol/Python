import os

# 1) Create a new directory "parent"
os.mkdir("parent")

# 2) Change current path to the new directory "parent"
os.chdir("parent")

# 3) Create three subdirectories under the "parent" directory: c1, c2, c3
subdirectories = ["c1", "c2", "c3"]
for subdir in subdirectories:
    os.mkdir(subdir)

# 4) Show the directory list of "parent"
directory_list = os.listdir()
print("Directory list of 'parent':", directory_list)
