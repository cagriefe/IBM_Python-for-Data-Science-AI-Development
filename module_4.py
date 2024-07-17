import urllib.request
import requests
import pandas as pd

# Define the URL and filename
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'example1.txt'

# Download the file using urllib
urllib.request.urlretrieve(url, filename)
print("File downloaded using urllib")

# Alternative method using requests
def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
    else:
        print(f"Failed to download file: {response.status_code}")

# Download the file using requests
download_file(url, filename)
print("File downloaded using requests")

# Read the file into a pandas DataFrame
df = pd.read_csv(filename)
print(df.head())



# Read the Example1.txt
example1 = "example1.txt"
file1 = open(example1, "r")


# Print the path of file
file1.name

# Print the mode of file, either 'r' or 'w'
file1.mode

# Read the file
FileContent = file1.read()
FileContent


# Print the file with '\n' as a new line
print(FileContent)

# Type of file content
type(FileContent)

# Close file after finish
file1.close()



## better way to open a file

# Open file using with
with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)

# Verify if the file is closed
file1.closed

# See the content of file
print(FileContent)

# Read first four characters
with open(example1, "r") as file1:
    print(file1.read(4))
    

# Read certain amount of characters
with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))
    

# Read certain amount of characters
with open(example1, "r") as file1:
    print(file1.read(16))
    print(file1.read(5))
    print(file1.read(9))
    

# Read one line
with open(example1, "r") as file1:
    print("first line: " + file1.readline())

#example
with open(example1, "r") as file1:
    print(file1.readline(20)) # does not read past the end of line
    print(file1.read(20)) # Returns the next 20 chars


# Iterate through the lines
with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1
            
            
# Read all lines and save as a list
with open(example1, "r") as file1:
    FileasList = file1.readlines()
    
# Print the lines
FileasList[0]
FileasList[1]
FileasList[2]


### Write and Save Files

# Write line to file
exmp2 = 'Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")
    
# Read file
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())
    
# Write lines to file
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")
    
# Check whether write to file
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())


# Sample list of text
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
Lines


# Write the strings in the list to text file
with open('Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)
        
# Verify if writing to file is successfully executed
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
    

#However, note that setting the mode to w overwrites all the existing data in the file.
with open('Example2.txt', 'w') as writefile:
    writefile.write("Overwrite\n")
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())



##Appending files

# Write a new line to text file
with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")
    

# Verify if the new line is in the text file
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
    

##Additional modes
# r+ : Reading and writing. Cannot truncate the file.
# w+ : Writing and reading. Truncates the file.
# a+ : Appending and Reading. Creates a new file, if none exists. You dont have to dwell on the specifics of each mode for this lab.

#a+
with open('Example2.txt', 'a+') as testwritefile:
    testwritefile.write("This is line E\n")
    print(testwritefile.read())