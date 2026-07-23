from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
from preprocessing import clean_text

def create_tags(df):
    
    columns=['store','description','categories']

    for col in columns:
        df[col]=df[col].apply(clean_text)

        df['Tags']=df[columns].apply(lambda x: ",".join(x),axis=1)

        return df

def create_tfidf(df):

    vectorizer=TfidfVectorizer()
    matrix=vectorizer.fit_transform(df['Tags'])
    return vectorizer, matrix

def extract_images(df):

    df["images_url"] = df["images"].apply(
        lambda x: x[0].get("large") 
        if isinstance(x, list) and len(x) > 0 
        else None
    )

    return df


