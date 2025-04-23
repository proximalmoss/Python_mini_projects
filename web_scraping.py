from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# Find the first table
table = soup.find('table', {'class': 'wikitable'})

# Extract all the header titles from the table
world_titles = table.find_all('th')

# Print the titles
for title in world_titles:
    print(title.text.strip())

#creating a dataframe
df=pd.DataFrame(columns=world_titles)
print(df)

#finding the data from columns and saving in a dataframe
column_data=table.find_all('tr')

for row in column_data[1:]:
    row_data=row.find_all('td')
    individual_row_data=[data.text.strip() for data in row_data]

    length=len(df)
    df.loc[length]=individual_row_data

print(df)

#saving to a csv file
df.to_csv('largest_us_companies.csv', index=False)