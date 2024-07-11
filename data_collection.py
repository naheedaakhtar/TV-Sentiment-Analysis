from bs4 import BeautifulSoup
import requests

#Extract online script and begin parsing 
script_html=requests.get('https://imsdb.com/scripts/Social-Network,-The.html').text
soup = BeautifulSoup(script_html,'lxml')

# Store Mark's Dialogue
mark_dialogue=[]
current_speaker=None
# Iterate through <b> html tags - where character names are listed
for tag in soup.find_all('b'):
    #Extract speaker name
    speaker= tag.text.strip()
    #Check if Mark is the speaker
    if speaker=='MARK':
        dialogue=""
        next_speaker= tag.find_next_sibling()
        
    
#print(script_html)



