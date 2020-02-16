"""
Exercise 22*
Given a .txt file that has a list of a bunch of names, 
count how many of each name there are in the file, and print out the results to the screen. 
I have a .txt file for you, if you want to use it!

Extra:
Instead of using the namelist.txt file from above (or instead of, if you want the challenge), 
take this Train.txt file, and count how many of each “category” of each image there are. 
This text file is actually a list of files corresponding to the SUN database scene recognition database, 
and lists the file directory hierarchy for the images. 
Once you take a look at the first line or two of the file, it will be clear which part represents the 
scene category. 
To do this, you’re going to have to remember a bit about string parsing in Python 3. 

Topics:
Reading a file
Dictionaries

"""
# MS (better solution would return count of items as dictionary so that count can be used)
with open('namelist.txt', 'r') as f:
    content = f.read().split()

unique_items = list(set(content))
dic = {}
print(unique_items)
for i in unique_items:
    dic[i] = content.count(i)

print(dic)

# Extras:
print("*"*50)