# Project Imports
from bs4 import BeautifulSoup
import pandas as pd
import re
import requests
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

def scrape_script():
    ''' 
    Scrapes 'The Social Network' script from imsdb.com and extracts Mark's dialogue 
    Returns: pandas.DataFrame containing Mark's dialogue with 'Speaker' and 'Dialogue' columns
    '''
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
    return mark_dialogue



#Download NLTK packages 
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Create lemmatizer and stopwords function 
lemmatizer = WordNetLemmatizer()
stop_words= set(stopwords.words('english'))

def preprocess_text(text):
    '''
        Removes stop words and gets the 'lemma' or meaning of repeated words
        Returns: tokens, individual words with meanings from the script
    '''
    text = re.sub(r'[^a-z\s]', '', text.lower())
    tokens = word_tokenize(text)
    #Remove stop words and lemmatize
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return tokens 


print("Start script execution")
def process_script():
    # Scrape the script 
    print("wee")

    mark_dialogue = scrape_script()
    # Preprocess dialogue
    mark_dialogue['Tokens'] = mark_dialogue['Dialogue'].apply(preprocess_text)

    return mark_dialogue

if __name__ == "__main__":
    processed_dialogue = process_script()
    print(processed_dialogue)