### APIs and Data Collection

## APIs

# Pandas is an API

import pandas as pd
import matplotlib.pyplot as plt

dict_={'a':[11,21,31],'b':[12,22,32]}

# When you create a Pandas object with the dataframe constructor, in API lingo this is an "instance". The data in the dictionary is passed along to the pandas API. You then use the dataframe to communicate with the API.
df=pd.DataFrame(dict_)
type(df)

# When you call the method head the dataframe communicates with the API displaying the first few rows of the dataframe.
df.head()

# When you call the method mean, the API will calculate the mean and return the value.
df.mean()



## REST APIs

# It's quite simple to use the nba api to make a request for a specific team. We don't require a JSON, all we require is an id. This information is stored locally in the API. We import the module teams.
from nba_api.stats.static import teams
import matplotlib.pyplot as plt

def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

# The method get_teams() returns a list of dictionaries.
nba_teams = teams.get_teams()

# The dictionary key id has a unique identifier for each team as a value. Let's look at the first three elements of the list:
nba_teams[0:3]

# To make things easier, we can convert the dictionary to a table. First, we use the function one dict, to create a dictionary. We use the common keys for each team as the keys, the value is a list; each element of the list corresponds to the values for each team. We then convert the dictionary to a dataframe, each row contains the information for a different team.
dict_nba_team=one_dict(nba_teams)
df_teams=pd.DataFrame(dict_nba_team)
df_teams.head()

#Will use the team's nickname to find the unique id, we can see the row that contains the warriors by using the column nickname as follows:
df_warriors=df_teams[df_teams['nickname']=='Warriors']
df_warriors

# We can use the following line of code to access the first column of the DataFrame:
id_warriors=df_warriors[['id']].values[0][0]
# we now have an integer that can be used to request the Warriors information 
id_warriors



## Practice Project: GDP Data extraction and processing

#An international firm that is looking to expand its business in different countries across the world has recruited you. You have been hired as a junior Data Engineer and are tasked with creating a script that can extract the list of the top 10 largest economies of the world in descending order of their GDPs in Billion USD (rounded to 2 decimal places), as logged by the International Monetary Fund (IMF).

import numpy as np
import pandas as pd



# You can also use this section to suppress warnings generated by your code:
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')
URL="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

# Extract tables from webpage using Pandas. Retain table number 3 as the required dataframe.
tables = pd.read_html(URL)
df = tables[3]

# Replace the column headers with column numbers
df.columns = range(df.shape[1])

# Retain columns with index 0 and 2 (name of country and value of GDP quoted by IMF)
df = df[[0,2]]
# Retain the Rows with index 1 to 10, indicating the top 10 economies of the world.
df = df.iloc[1:11:]
# Assign column names as "Country" and "GDP (Million USD)"
df.columns = ['Country','GDP (Million USD)']
df

# Change the data type of the 'GDP (Million USD)' column to integer. Use astype() method.
df['GDP (Million USD)'] = df['GDP (Million USD)'].astype(int)

# Convert the GDP value in Million USD to Billion USD
df[['GDP (Million USD)']] = df[['GDP (Million USD)']]/1000

# Use numpy.round() method to round the value to 2 decimal places.
df[['GDP (Million USD)']] = np.round(df[['GDP (Million USD)']], 2)

# Rename the column header from 'GDP (Million USD)' to 'GDP (Billion USD)'
df.rename(columns = {'GDP (Million USD)' : 'GDP (Billion USD)'})

# Load the DataFrame to the CSV file named "Largest_economies.csv"
df.to_csv('./Largest_economies.csv')
df



## HTTP and Requests

# Requests
import requests

import os 
from PIL import Image
from IPython.display import IFrame

# You can make a GET request via the method get to www.ibm.com:
url='https://www.ibm.com/'
r=requests.get(url)

# We have the response object r, this has information about the request, like the status of the request. We can view the status code using the attribute status_code.
r.status_code

# You can view the request headers:
print(r.request.headers)

# You can view the request body, in the following line, as there is no body for a get request we get a None:
print("request body:", r.request.body)

# You can view the HTTP response header using the attribute headers. This returns a python dictionary of HTTP response headers.
header=r.headers
print(r.headers)

# We can obtain the date the request was sent using the key Date.
header['date']

# Content-Type indicates the type of data:
header['Content-Type']

# You can also check the encoding:
r.encoding

# As the Content-Type is text/html we can use the attribute text to display the HTML in the body. We can review the first 100 characters:
r.text[0:100]


# Use single quotation marks for defining string
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'

# We can make a get request:
r=requests.get(url)

# We can look at the response header:
print(r.headers)

# We can see the 'Content-Type'
r.headers['Content-Type']

# An image is a response object that contains the image as a bytes-like object. As a result, we must save it using a file object. First, we specify the file path and name
path=os.path.join(os.getcwd(),'image.png')

# We save the file, in order to access the body of the response we use the attribute content then save it using the open function and write method:
with open(path,'wb') as f:
    f.write(r.content)

# We can view the image:
Image.open(path)



#Write the commands to download the txt file in the given link.
URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'

path = os.path.join(os.getcwd(), 'content1.txt')
r = requests.get(URL)
with open(path, 'wb') as f:
    f.write(r.content)
    
    
import json    
## Get Request with URL Parameters

url_get='http://httpbin.org/get'

# A query string is a part of a uniform resource locator (URL), this sends other information to the web server. The start of the query is a ?, followed by a series of parameter and value pairs, as shown in the table below. The first parameter name is name and the value is Joseph. The second parameter name is ID and the Value is 123. Each pair, parameter, and value is separated by an equals sign, =. The series of pairs is separated by the ampersand &.

# To create a Query string, add a dictionary. The keys are the parameter names and the values are the value of the Query string.
payload={"name":"Joseph","ID":"123"}

# Then passing the dictionary payload to the params parameter of the  get() function:
r=requests.get(url_get,params=payload)

# We can print out the URL and see the name and values.
r.url

# There is no request body.
print("request body:", r.request.body)

# We can print out the status code.
print(r.status_code)

# We can view the response as text:
print(r.text)

# We can look at the 'Content-Type'.
r.headers['Content-Type']

# As the content 'Content-Type' is in the JSON format we can use the method json(), it returns a Python dict:
r.json()

# The key args has the name and values:
r.json()['args']



## Post Requests

# Like a GET request, a POST is used to send data to a server, but the POST request sends the data in a request body. In order to send the Post Request in Python, in the URL we change the route to POST:
url_post='http://httpbin.org/post'

# To make a POST request we use the post() function, the variable payload is passed to the parameter  data :
r_post=requests.post(url_post,data=payload)

# Comparing the URL from the response object of the GET and POST request we see the POST request has no name or value pairs.
print("POST request URL:",r_post.url )
print("GET request URL:",r.url)

# We can compare the POST and GET request body, we see only the POST request has a body:
print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)

# We can view the form as well:
r_post.json()['form']



## Random User and Fruityvice API Examples

# Objectives
# After completing this lab you will be able to:

# Load and use RandomUser API, using RandomUser() Python library
# Load and use Fruityvice API, using requests Python library
# Load and use Open-Joke-API, using requests Python library


# # RandomUser API

from randomuser import RandomUser
import pandas as pd

# First, we will create a random user object, r.
r = RandomUser()


# Then, using generate_users() function, we get a list of random 10 users.
some_list = r.generate_users(10)
some_list = r.generate_users(10)
some_list

# The "Get Methods" functions mentioned at the beginning of this notebook, can generate the required parameters to construct a dataset. For example, to get full name, we call get_full_name() function.
name = r.get_full_name()
name = r.get_full_name()

# Let's say we only need 10 users with full names and their email addresses. We can write a "for-loop" to print these 10 users.
for user in some_list:
    print (user.get_full_name()," ",user.get_email())
    

# Generate photos of the random 10 users.
for user in some_list:
    print (user.get_picture())
    
    

# To generate a table with information about the users
def get_users():
    users =[]
     
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)

get_users()
df1 = pd.DataFrame(get_users())
df1



# # Fruityvice API
import requests
import json

# We will obtain the fruityvice API data using requests.get("url") function. The data is in a json format.
data = requests.get("https://fruityvice.com/api/fruit/all")

# We will retrieve results using json.loads() function.
results = json.loads(data.text)

# We will convert our json data into pandas data frame.
pd.DataFrame(results)

# The result is in a nested json format. The 'nutrition' column contains multiple subcolumns, so the data needs to be 'flattened' or normalized.
df2 = pd.json_normalize(results)
df2



## Web Scraping 

from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

#Beautiful Soup is a Python library for pulling data out of HTML and XML files, we will focus on HTML files. This is accomplished by representing the HTML as a set of objects with methods used to parse the HTML.  We can navigate the HTML as a tree, and/or filter out what we are looking for.
#Consider the following HTML:
html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3> \
<b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p> \
<h3>Stephen Curry</h3><p> Salary: $85,000,000</p> \
<h3>Kevin Durant</h3><p> Salary: $73,200,000</p></body></html>"

# To parse a document, pass it into the <code>BeautifulSoup</code> constructor. The <code>BeautifulSoup</code> object represents the document as a nested data structure:
soup = BeautifulSoup(html, 'html5lib')

# We can use the method <code>prettify()</code> to display the HTML in the nested structure:
print(soup.prettify())



## Tags

# Let's say we want the  title of the page and the name of the top paid player. We can use the <code>Tag</code>. The <code>Tag</code> object corresponds to an HTML tag in the original document, for example, the tag title.
tag_object = soup.title
print("tag object:", tag_object)

# we can see the tag type <code>bs4.element.Tag</code>
print("tag object type:", type(tag_object))

# If there is more than one <code>Tag</code> with the same name, the first element with that <code>Tag</code> name is called. This corresponds to the most paid player:
tag_object = soup.h3
tag_object


## Children, Parents, and Siblings

# As stated above, the Tag object is a tree of objects. We can access the child of the tag or navigate down the branch as follows:
tag_child = tag_object.b
tag_child

# You can access the parent with the parent.
parent_tag = tag_child.parent
parent_tag

#tag_object parent is the body element.
tag_object.parent

#<code>tag_object</code> sibling is the <code>paragraph</code> element.
sibling_1 = tag_object.next_sibling
sibling_1

#`sibling_2` is the `header` element, which is also a sibling of both `sibling_1` and `tag_object`
sibling_2 = sibling_1.next_sibling
sibling_2


### Filter
# Filters allow you to find complex patterns, the simplest filter is a string. In this section we will pass a string to a different filter method and Beautiful Soup will perform a match against that exact string. Consider the following HTML of rocket launches:
table = "<table><tr><td id='flight'>Flight No</td><td>Launch site</td> \
<td>Payload mass</td></tr><tr> <td>1</td> \
<td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td> \
<td>300 kg</td></tr><tr><td>2</td> \
<td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td> \
<td>94 kg</td></tr><tr><td>3</td> \
<td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td> \
<td>80 kg</td></tr></table>"

table_bs = BeautifulSoup(table, 'html5lib')

## find_All
# The <code>find_all()</code> method looks through a tag's descendants and retrieves all descendants that match your filters.
# The Method signature for <code>find_all(name, attrs, recursive, string, limit, **kwargs)<c/ode>

## Name
# When we set the <code>name</code> parameter to a tag name, the method will extract all the tags with that name and its children.

table_rows = table_bs.find_all('tr')
table_rows

# The result is a Python iterable just like a list, each element is a <code>tag</code> object:
first_row = table_rows[0]
first_row

# The type is tag
print(type(first_row))

# If we iterate through the list, each element corresponds to a row in the table:
for i, row in enumerate(table_rows):
    print("row", i, "is", row)
    

# As <code>row</code> is a <code>cell</code> object, we can apply the method <code>find_all</code> to it and extract table cells in the object <code>cells</code> using the tag <code>td</code>, this is all the children with the name <code>td</code>. The result is a list, each element corresponds to a cell and is a <code>Tag</code> object, we can iterate through this list as well. We can extract the content using the <code>string</code> attribute.

for i, row in enumerate(table_rows):
    print("row", i)
    cells = row.find_all('td')
    for j, cell in enumerate(cells):
        print('colunm', j, "cell", cell)
        
        
## Attributes
# If the argument is not recognized it will be turned into a filter on the tag's attributes. For example with the <code>id</code> argument, Beautiful Soup will filter against each tag's <code>id</code> attribute. For example, the first <code>td</code> elements have a value of <code>id</code> of <code>flight</code>, therefore we can filter based on that <code>id</code> value.

table_bs.find_all(id="flight")

# We can find all the elements that have links to the Florida Wikipedia page:

list_input = table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
list_input

# If we set the <code>href</code> attribute to True, regardless of what the value is, the code finds all anchor tags with <code>href</code> value:
table_bs.find_all('a', href=True)



### string

# With string you can search for strings instead of tags, where we find all the elments with Florida:
table_bs.find_all(string="Florida")



### Find

two_tables="<h3>Rocket Launch </h3> \
<p><table class='rocket'> \
<tr><td>Flight No</td><td>Launch site</td><td>Payload mass</td></tr> \
<tr><td>1</td><td>Florida</td><td>300 kg</td></tr> \
<tr><td>2</td><td>Texas</td><td>94 kg</td></tr> \
<tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p>\
<p><h3>Pizza Party</h3> \
<table class='pizza'> \
<tr><td>Pizza Place</td><td>Orders</td><td>Slices </td></tr> \
<tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr> \
<tr><td>Little Caesars</td><td>12</td><td >144 </td></tr> \
<tr><td>Papa John's</td><td>15 </td><td>165</td></tr>"

#We create a <code>BeautifulSoup</code> object  <code>two_tables_bs</code>
two_tables_bs = BeautifulSoup(two_tables, 'html.parser')

#We can find the first table using the tag name table
two_tables_bs.find("table")

# We can filter on the class attribute to find the second table, but because class is a keyword in Python, we add an underscore to differentiate them.
two_tables_bs.find("table", class_='pizza')



### Downloading And Scraping The Contents Of A Web Page

url = "http://www.ibm.com"

# We use <code>get</code> to download the contents of the webpage in text format and store in a variable called <code>data</code>:
data = requests.get(url).text

# We create a <code>BeautifulSoup</code> object using the <code>BeautifulSoup</code> constructor
soup = BeautifulSoup(data, "html5lib")  # create a soup object using the variable 'data'

# Scrape all links
for link in soup.find_all('a', href=True):  # in html anchor/link is represented by the tag <a>
    print(link.get('href'))
    

# Scrape all images Tags
for link in soup.find_all('img'):  # in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))
    
## Scrape data from HTML tables
# The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

# Before proceeding to scrape a web site, you need to examine the contents and the way data is organized on the website. Open the above url in your browser and check how many rows and columns there are in the color table.
# get the contents of the webpage in text format and store in a variable called data
data = requests.get(url).text

soup = BeautifulSoup(data, "html5lib")

# find a html table in the web page
table = soup.find('table')  # in html table is represented by the tag <table>

# Get all rows from the table
for row in table.find_all('tr'):  # in html table row represented by tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td')  # in html a column is represented by tag <td>
    color_name = cols[2].string  # store the value in column 3 as color_name
    color_code = cols[3].text  # store the value in column 4 as color_code
    print("{}--->{}".format(color_name, color_code))
    
    
    
## Scraping tables from a Web page using Pandas

#Particularly for extracting tabular data from a web page, you may also use the `read_html()` method of the Pandas library. 

# The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

#You may extract all the tables from the given webpage simply by using the following commands.
import pandas as pd

tables = pd.read_html(url)
tables

#`tables` is now a list of dataframes representing the tables from the web page, in the sequence of their appearance. In the current  URL, there is only a single table, so the same can be accessed as shown below.
tables[0]



### Different file formats

# Comma-separated values (CSV) file format

# Reading data from CSV in Python

# The Pandas Library is a useful tool that enables us to read various datasets into a Pandas data frame
import pandas as pd

df = pd.read_csv("addresses.csv", header=None)
df

# Adding column name to the DataFrame
df.columns =['First Name', 'Last Name', 'Location ', 'City','State','Area Code']
df

# Selecting a single column
df['First Name']

# Selecting multiple columns
df = df[['First Name', 'Last Name', 'Location ', 'City','State','Area Code']]
df

# Selecting rows using .iloc and .loc
# To select the first row
df.loc[0]

# To select the 0th,1st and 2nd row of "First Name" column only
df.loc[[0,1,2], "First Name" ]

# To select the 0th,1st and 2nd row of "First Name" column only
df.iloc[[0,1,2], 0]



## Transform Function in Pandas
# import library
import pandas as pd
import numpy as np

# creating a dataframe
df=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
df

# applying the transform function
df = df.transform(func = lambda x : x + 10)
df

# Now we will use DataFrame.transform() function to find the square root to each element of the dataframe.
result = df.transform(func = ['sqrt'])



### JSON file Format

# JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write.

import json

## Writing JSON to a File

person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

# serialization using dump() function

# json.dump() method can be used for writing to JSON file.

# Syntax: json.dump(dict, file_pointer)

# Parameters:

# dictionary – name of the dictionary which should be converted to JSON object.
# file pointer – pointer of the file opened in write or append mode.

with open('person.json', 'w') as f:  # writing JSON object
    json.dump(person, f)
    

# serialization using dumps() function
# json.dumps() that helps in converting a dictionary to a JSON object.

# It takes two parameters:

# dictionary – name of the dictionary which should be converted to JSON object.
# indent – defines the number of units for indentation

# Serializing json  
json_object = json.dumps(person, indent = 4) 
  
# Writing to sample.json 
with open("sample.json", "w") as outfile: 
    outfile.write(json_object)
    
print(json_object)


## Reading JSON to a File
# Using json.load()
# The JSON package has json.load() function that loads the json content from a json file into a dictionary.

# It takes one parameter:

# File pointer : A file pointer that points to a JSON file.

import json 
  
# Opening JSON file 
with open('sample.json', 'r') as openfile: 
  
    # Reading from json file 
    json_object = json.load(openfile) 
  
print(json_object) 
print(type(json_object))



### XLSX file format

## Reading the data from XLSX file

import urllib.request
import pandas as pd

urllib.request.urlretrieve("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx", "sample.xlsx")

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

df = pd.read_excel("file_example_XLSX_10.xlsx")
df


### XML file format

# XML is also known as Extensible Markup Language

## Writing with xml.etree.ElementTree

import xml.etree.ElementTree as ET

# create the file structure
employee = ET.Element('employee')
details = ET.SubElement(employee, 'details')
first = ET.SubElement(details, 'firstname')
second = ET.SubElement(details, 'lastname')
third = ET.SubElement(details, 'age')
first.text = 'Shiv'
second.text = 'Mishra'
third.text = '23'

# create a new XML file with the results
mydata1 = ET.ElementTree(employee)
# myfile = open("items2.xml", "wb")
# myfile.write(mydata)
with open("new_sample.xml", "wb") as files:
    mydata1.write(files)
 
 
 
    
## Reading with xml.etree.ElementTree

import xml.etree.ElementTree as etree
import pandas as pd

tree = etree.parse("Sample-employee-XML-file.xml")

root = tree.getroot()
columns = ["firstname", "lastname", "title", "division", "building","room"]

datatframe = pd.DataFrame(columns = columns)

for node in root: 

    firstname = node.find("firstname").text

    lastname = node.find("lastname").text 

    title = node.find("title").text 
    
    division = node.find("division").text 
    
    building = node.find("building").text
    
    room = node.find("room").text
    
    datatframe = pd.concat([datatframe, pd.Series([firstname, lastname, title, division, building, room], index = columns)], ignore_index = True)

datatframe


## Reading xml file using pandas.read_xml function
# Herein xpath we mention the set of xml nodes to be considered for migrating  to the dataframe which in this case is details node under employees.
df=pd.read_xml("Sample-employee-XML-file.xml", xpath="/employees/details") 
df


### Save Data

datatframe.to_csv("employee.csv", index=False)
df = pd.read_csv("employee.csv")
df



### Read/Save Other Data Formats

## Binary File Format

# Reading the Image file

# importing PIL 
from PIL import Image 

# Uncomment if running locally
import urllib.request
urllib.request.urlretrieve("https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg", "dog.jpg")

filename = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

download(filename, "./dog.jpg")

# Read image 
img = Image.open('./dog.jpg','r') 
  
# Output Images 
img.show()



### Data Analysis

# Import pandas library
import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"
async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

download(filename, "diabetes.csv")
df = pd.read_csv("diabetes.csv")
df


# After reading the dataset, we can use the dataframe.head(n) method to check the top n rows of the dataframe, where n is an integer. Contrary to dataframe.head(n), dataframe.tail(n) will show you the bottom n rows of the dataframe.

# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe") 
df.head(5)

# To view the dimensions of the dataframe, we use the .shape parameter.
df.shape



### Statistical Overview of dataset

# This method prints information about a DataFrame including the index dtype and columns, non-null values and memory usage.
df.info()

# Pandas describe() is used to view some basic statistical details like percentile, mean, standard deviation, etc. of a data frame or a series of numeric values. When this method is applied to a series of strings, it returns a different output
df.describe()



### Identify and handle missing values
# We use Python's built-in functions to identify these missing values. There are two methods to detect missing data:

# .isnull()

# .notnull()

# The output is a boolean value indicating whether the value that is passed into the argument is in fact missing data.

missing_data = df.isnull()
missing_data.head(5)



## Correct data format

# Check all data is in the correct format (int, float, text or other).

# In Pandas, we use

# .dtype() to check the data type

# .astype() to change the data type

# Numerical variables should have type 'float' or 'int'.


# As we can see below, All columns have the correct data type.
df.dtypes



### Visualization

# Visualization is one of the best way to get insights from the dataset. Seaborn and Matplotlib are two of Python's most powerful visualization libraries.
# import libraries
import matplotlib.pyplot as plt
import seaborn as sns

labels= 'Not Diabetic','Diabetic'
plt.pie(df['Outcome'].value_counts(),labels=labels,autopct='%0.02f%%')
plt.legend()
plt.show()