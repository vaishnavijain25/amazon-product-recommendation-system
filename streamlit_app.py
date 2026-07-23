import streamlit as st
import joblib
from scipy import sparse

from src.recommender import recommend

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Amazon Electronics Recommendation System",
    page_icon="🛍️",
    layout="wide"
)

# -------------------------------
# Load Models
# -------------------------------
@st.cache_resource
def load_models():
    df = joblib.load("models/products.pkl")
    matrix = sparse.load_npz("models/tfidf_matrix.npz")
    return df, matrix

df, matrix = load_models()

# -------------------------------
# Custom CSS (For styling titles and headers)
# -------------------------------
st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 4rem !important;  /* Significantly larger main title */
    font-weight: 800;
    color: #1565C0;
    margin-bottom: 0px;
    line-height: 1.2;
}
.subtitle {
    text-align: center;
    font-size: 1.5rem !important; /* Larger subtitle */
    color: #B0BEC5;               /* Lighter gray for better visibility in dark mode */
    margin-top: 10px;
    margin-bottom: 35px;
    font-weight: 400;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Header
# -------------------------------
st.markdown("<h1 class='main-title'>Amazon Electronics Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Content Based Recommendation using TF-IDF & Cosine Similarity</p>", unsafe_allow_html=True)
# -------------------------------
# Search Section
# -------------------------------
col1, col2 = st.columns([4, 1])

with col1:
    product_name = st.text_input("Enter Product Name")

with col2:
    top_n = st.number_input("Recommendations", min_value=1, max_value=20, value=10)

search = st.button("Recommend")

# -------------------------------
# Recommendation Section
# -------------------------------
if search:
    try:
        recommendations = recommend(df, matrix, product_name, top_n)
        st.success(f"Showing Top {top_n} Recommendations")

        # Create 3 columns for grid layout
        cols = st.columns(3)

        for i, (_, row) in enumerate(recommendations.iterrows()):
            with cols[i % 3]:
                # Native container with a border serves perfectly as a product card
                with st.container(border=True):
                    
                    # Image layout adjustment
                    if row["images_url"]:
                        # Adjust 'width' as needed (e.g., 150 or 200). 
                        # Or use use_container_width=True to make it stretch.
                        st.image(row["images_url"], width=150)
                    else:
                        st.info("No Image Available")

                    st.markdown(f"### {row['title']}")
                    st.write(f"**Store :** {row['store']}")
                    st.write(f"**Price :** {row['price']}")
                    st.write(f"**Rating :** ⭐ {row['average_rating']}")
                    st.write(f"**Reviews :** {row['rating_number']}")

    except Exception as e:
        st.error(f"No Products found")