import spacy 
from spacy.lang.en.stop_words import STOP_WORDS

nlp= spacy.load("en_core_web_sm")

def fill_missing_values(df):

    df['main_category']= df['main_category'].fillna("Unknown")
    df['store']= df['store'].fillna("Unknown")
    df['price']= df['price'].fillna("Not Available")

    return df

def convert_list(df):

    df['description']=df['description'].apply(lambda x: ' '.join(x) if isinstance(x,list) else x)
    df['categories']=df['categories'].apply(lambda x: ' '.join(x) if isinstance(x,list) else x)

    return df

def clean_text(text):
    
    doc=nlp(str(text).lower())

    tags=[token.text for token in doc if token.text.isalnum() and token.text not in STOP_WORDS]

    return ",".join(tags)
    

