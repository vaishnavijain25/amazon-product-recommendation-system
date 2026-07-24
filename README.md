# 🛍️ Amazon Product Recommendation System

**Content-Based Product Recommendation using TF-IDF and Cosine Similarity**

---

# 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Business Objective](#-business-objective)
- [Dataset](#-dataset)
- [Exploratory Data Analysis (EDA)](#-exploratory-data-analysis-eda)
- [Recommendation Methodology](#️-recommendation-methodology)
- [Streamlit Application](#️-streamlit-application)
- [Technologies Used](#️-technologies-used)
- [Project Structure](#-project-structure)
- [How to Run This Project](#-how-to-run-this-project)
- [Application Preview](#-application-preview)
- [Future Improvements](#-future-improvements)
- [Author & Contact](#-author--contact)

---

# 📌 Project Overview

This project implements an **end-to-end Content-Based Recommendation System** for Amazon Electronics products.

The system recommends similar products by analyzing product information such as:

- Product descriptions
- Categories
- Store information

The recommendation engine uses **Natural Language Processing (NLP)** techniques with **TF-IDF Vectorization** and **Cosine Similarity** to identify similar products.

The complete pipeline is deployed using an interactive **Streamlit web application**.

---

# 🎯 Business Objective

## 🛍️ Product Recommendation

### Objective

Recommend similar electronics products based on product content instead of user purchase history.

### Why it matters

- Improve product discovery
- Enhance customer shopping experience
- Help users find similar products quickly
- Increase product visibility
- Provide relevant product suggestions

---

# 📂 Dataset

This project uses the **Amazon Electronics Product Metadata Dataset**.

The dataset contains:

- Product Title
- Product Description
- Categories
- Store
- Price
- Average Rating
- Number of Ratings
- Product Images

> Note: Dataset and generated model files are not included in this repository due to GitHub file size limitations.

## Dataset Download

Download the **Electronics Metadata (`meta_Electronics.jsonl`)** dataset from the official repository:

**Dataset Link:** https://amazon-reviews-2023.github.io/#

After downloading, place the file inside:

```text
Data/
└── meta_Electronics.jsonl
```

---

# 📊 Exploratory Data Analysis (EDA)

EDA was performed to understand the product dataset before building the recommendation system.

Analysis includes:

- Dataset overview
- Missing value analysis
- Product category distribution
- Store distribution
- Rating distribution
- Price analysis
- Text feature exploration

EDA insights helped in designing preprocessing and feature engineering steps.

---

# ⚙️ Recommendation Methodology

The recommendation pipeline consists of the following steps:

## 1. Data Loading

Load Amazon Electronics product metadata using Pandas.

## 2. Data Preprocessing

Performed:

- Missing value handling
- List to text conversion
- Text normalization
- Stop word removal
- Token filtering using SpaCy

## 3. Feature Engineering

Created a combined **Tags** feature using:

- Store
- Description
- Categories

## 4. TF-IDF Vectorization

Converted product text information into numerical vectors using:

**TF-IDF Vectorizer**

## 5. Cosine Similarity

Calculated similarity between products using cosine similarity scores.

## 6. Top-N Recommendation

Returned the most similar products based on similarity ranking.

---

# 🖥️ Streamlit Application

The project includes an interactive Streamlit application.

## Features

- 🔍 Product search
- 🛒 Similar product recommendations
- ⭐ Product ratings display
- 💰 Price information
- 🏬 Store information
- 🖼️ Product images
- ⚡ Fast recommendation generation

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- SpaCy
- SciPy
- Joblib
- Streamlit

---

# 📁 Project Structure

```text
amazon-product-recommendation-system/
│
├── Data/
│
├── models/
│
├── notebooks/
│   └── EDA.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   └── recommender.py
│
├── main_pipeline.py
├── streamlit_app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 How to Run This Project

## 1. Clone Repository

```bash
git clone https://github.com/vaishnavijain25/amazon-product-recommendation-system.git
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Install SpaCy Model

```bash
python -m spacy download en_core_web_sm
```

## 4. Add Dataset

Place dataset:

```text
Data/
└── meta_Electronics.jsonl
```

## 5. Generate Model Files

Run:

```bash
python main_pipeline.py
```

This creates:

```text
models/
├── products.pkl
├── tfidf_matrix.npz
└── tfidf_vectorizer.pkl
```

## 6. Run Application

```bash
streamlit run streamlit_app.py
```

---

# 📸 Application Preview

## Home Page

<img width="1872" height="967" alt="Screenshot 2026-07-24 080245" src="https://github.com/user-attachments/assets/0bb584cc-be95-4f08-a93f-5109cfca2c62" />


## Recommendation Results

<img width="1877" height="912" alt="Screenshot 2026-07-24 082419" src="https://github.com/user-attachments/assets/1dc93c40-ab9e-436e-8a95-7f8b0315bdcd" />


---

# 🔮 Future Improvements

- Hybrid Recommendation System
- Collaborative Filtering
- Personalized Recommendations
- Search Autocomplete
- FastAPI Backend
- Docker Deployment
- Cloud Deployment

---

# 👩‍💻 Author & Contact

**Vaishnavi Jain**

Aspiring Data Scientist | Machine Learning Enthusiast

📧 Email: vaishnavijain25@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/vaishnavi-jain-60764723b/

🌐 GitHub: https://github.com/vaishnavijain25
