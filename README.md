# 🎬 IMDb 2024 Movie Recommendation System

This project is a **content-based movie recommendation system** using **NLP techniques** and a **Streamlit interface**. Given a movie **storyline input** from the user, it returns the top 5 similar movies from the **IMDb 2024 dataset**, scraped directly using **Selenium**.

## 📁 Project Structure
├── imdb_2024_movies.csv # Scraped movie data (Movie Name, Storyline)
├── scraper.py # Selenium-based web scraping script
├── preprocess.py # NLP + recommendation logic (TF-IDF + Cosine Similarity)
├── app.py # Streamlit frontend application
├── README.md # Project overview and instructions
├── requirements.txt # All required Python dependencies
└── project_documentation.pdf # Complete project report



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
git clone https://github.com/yourusername/imdb-2024-recommender.git
cd imdb-2024-recommender
