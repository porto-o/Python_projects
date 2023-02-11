# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
#
# You are going to create a list called result which contains the numbers that are common in both files.

data_f1 = open("file1.txt")
list_data_1 = data_f1.readlines()

data_f2 = open("file2.txt")
list_data_2 = data_f2.readlines()

result = [int(number) for number in list_data_1 if number in list_data_2]
print(result)
