from sklearn.metrics.pairwise import cosine_similarity

def recommend(df, matrix, title, top_n=10):

    matched = df[
        df["title"].str.contains(title, case=False, na=False)
    ]

    if matched.empty:
        return None

    index = matched.index[0]

    # Compare only one product with all products
    similarity = cosine_similarity(
        matrix[index],
        matrix
    ).flatten()

    indices = similarity.argsort()[::-1][1:top_n+1]

    return df.iloc[indices][
        [
            "title",
            "store",
            "price",
            "average_rating",
            "rating_number",
            "images_url"
        ]
    ]