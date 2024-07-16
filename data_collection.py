'''Utilize webscraping package BeautifulSoup to parse through 
"The Social Network" script from imsdb.com
'''
from bs4 import BeautifulSoup
import pandas as pd
import requests

#Extract online script and begin parsing 
script_html=requests.get('https://imsdb.com/scripts/Social-Network,-The.html').text
soup = BeautifulSoup(script_html,'html.parser')

# Store Mark's Dialogue
mark_dialogue=pd.DataFrame(columns=['Speaker','Dialogue'])

# Iterate through <b> html tags - where character names are listed
for tag in soup.find_all('b'):
    #Extract speaker name
    speaker= tag.get_text(strip=True)
    dialogue=''
    next_element=tag.next_sibling
   
    # Iterate until next speaker <b> tag 
    while next_element and (next_element.name!='b' if next_element.name else True):
        # Add text content, strip extra spaces and newlines
        if next_element.name is None:
            dialogue+=next_element.strip() + ' '
        next_element= next_element.next_sibling
    # Add to dataframe
    if dialogue.strip() and speaker == 'MARK':
        mark_dialogue = mark_dialogue.append({'Speaker': speaker,'Dialogue': dialogue.strip()}, ignore_index=True)

print(mark_dialogue)



