import joblib
from scipy import sparse

from data_loader import load_data
from preprocessing import (fill_missing_values,convert_list)
from feature_engineering import (create_tags,create_tfidf,extract_images)

DATA_PATH=r'E:\DATA SCIENCE AND AI\Amazon Product Recommendation System\Data\meta_Electronics.jsonl'

def pipeline():

    print("Loading data....")

    df=load_data(DATA_PATH,nrows=50000)

    print("Precprocessing....")

    df= fill_missing_values(df)
    df=convert_list(df)

    print("Creating images url....")

    df=extract_images(df)

    print("Creating tags....")

    df=create_tags(df)

    print("Creating TF-IDF matrix....")

    vectorizer,tfidf_matrix=create_tfidf(df)

    print("Saving models....")

    joblib.dump(vectorizer,"models/tfidf_vectorizer.pkl")

    joblib.dump(df,'models/products.pkl')

    sparse.save_npz("models/tfidf_matrix.npz",tfidf_matrix)

    print("Pipeline completed successfully!")

if __name__ == "__main__":
    pipeline()
