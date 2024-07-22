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