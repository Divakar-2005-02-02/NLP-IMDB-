# 🎬 IMDb 2024 Movie Recommendation System

This project is a **content-based movie recommendation system** using **NLP techniques** and a **Streamlit interface**. Given a movie **storyline input** from the user, it returns the top 5 similar movies from the **IMDb 2024 dataset**, scraped directly using **Selenium**.

## 📁 Project Structure

```
├── imdb_2024_movies.csv          # Scraped movie data (Movie Name, Storyline)
├── scraper.py                    # Selenium-based web scraping script
├── preprocess.py                 # NLP + recommendation logic (TF-IDF + Cosine Similarity)
├── app.py                        # Streamlit frontend application
├── README.md                     # Project overview and instructions
├── requirements.txt              # All required Python dependencies
└── project_documentation.pdf     # Complete project report
```

---

## 🚀 Features

- Scrapes the latest IMDb movies (2024) including title and storyline
- Preprocesses text with NLTK (cleaning, stopword removal, tokenization)
- Converts text into vectors using **TF-IDF**
- Calculates similarity using **Cosine Similarity**
- Suggests the **top 5 similar movies** based on user input
- Built with an interactive **Streamlit** user interface

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Divakar-2005-02-02/NLP-IMDB-.git
cd NLP-IMDB-
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download NLTK Resources

```python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

---

## 🧠 Usage

### Step 1: Scrape IMDb Data

Make sure you have ChromeDriver installed and update its path in `scraper.py`.

```bash
python scraper.py
```

This generates `imdb_2024_movies.csv`.

### Step 2: Launch the Streamlit App

```bash
streamlit run app.py
```

### Step 3: Enter Your Own Movie Storyline

On the Streamlit UI, paste a custom movie storyline and get 5 similar IMDb 2024 movies recommended based on NLP similarity!

---

## 📊 Example Input

```
A skilled thief is given a chance at redemption if he can successfully perform one last job: stealing an idea from someone's subconscious.
```

## 📌 Sample Output

```
Top 5 Recommended Movies:
1. Inception
2. Tenet
3. Interstellar
4. The Prestige
5. Shutter Island
```

---

## 🛠️ Tools Used

- Python 3.10+
- Selenium
- Pandas
- NLTK
- Scikit-learn
- Streamlit

---

## 📑 Project Report

See `project_documentation.pdf` for full details on methodology, scraping, testing, screenshots, and future work.

---
