# 🎬 MovieGenie: GenAI-Powered Movie Recommendation System

A sophisticated movie recommendation system that uses natural language processing, semantic search, and explainable AI to provide personalized movie suggestions.

## ✨ Features

- **Natural Language Understanding**: Describe what you feel like watching in plain English
- **Semantic Search**: Uses embeddings and FAISS for intelligent movie matching
- **Explainable AI**: Get detailed explanations for why each movie is recommended
- **Beautiful UI**: Modern, responsive Streamlit interface with movie posters
- **Rich Dataset**: Curated collection of movies with comprehensive metadata
- **Interactive Cards**: Expandable movie cards with detailed information

## 🏗️ Architecture

```
MovieGenie/
├── backend/                 # AI processing components
│   ├── Embedding.py        # Text-to-vector conversion
│   ├── VectorDB.py         # FAISS similarity search
│   ├── LLM.py             # Gemini AI integration
│   ├── PromptTemplate.py  # LLM prompt engineering
│   ├── Recommender.py     # Main orchestration
│   └── Thunking.py        # Text processing utilities
├── frontend/               # User interface
│   └── app.py             # Streamlit web application
├── data/                   # Movie dataset
│   └── movies.csv         # Movie metadata and posters
├── fetch_tmdb_movies.py   # Data collection script
└── requirements.txt       # Python dependencies
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google API Key (for Gemini AI)
- TMDB API Key (optional, for data collection)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/divyanshsharma2003/Movie-Rec-Model.git
   cd Movie-Rec-Model
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # or
   source .venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   TMDB_API_KEY=your_tmdb_api_key_here  # Optional
   ```

5. **Run the application**
   ```bash
   streamlit run frontend/app.py
   ```

## 🎯 Usage

1. **Start the app**: The Streamlit interface will open in your browser
2. **Describe your mood**: Enter natural language queries like:
   - "A slow-paced emotional sci-fi like Interstellar"
   - "Something funny and lighthearted for a date night"
   - "A thrilling mystery that keeps me guessing"
3. **Get recommendations**: Click "Recommend" to see AI-powered suggestions
4. **Explore details**: Click the ➕ button to expand movie cards for more information

## 🔧 Technical Details

### AI Components

- **Embeddings**: SentenceTransformer (all-MiniLM-L6-v2) for semantic text understanding
- **Vector Database**: FAISS for fast similarity search across movie embeddings
- **Language Model**: Google Gemini 1.5 Flash for generating explainable recommendations
- **Prompt Engineering**: Structured prompts for consistent, safe AI responses

### Data Pipeline

1. **Data Collection**: TMDB API integration for rich movie metadata
2. **Embedding Generation**: Movie summaries converted to semantic vectors
3. **Query Processing**: User input embedded and matched against movie database
4. **Recommendation Generation**: LLM creates personalized explanations

### Frontend Features

- **Responsive Design**: Works on desktop and mobile devices
- **Dark Theme**: Modern UI with blue accent colors
- **Interactive Cards**: Expandable movie information with smooth animations
- **Session Management**: Maintains state across interactions

## 📊 Dataset

The system includes a curated dataset of movies with:
- **Title, Summary, Year, Genre**
- **Director, Cast, Duration**
- **Language, Country, Poster URLs**
- **Comprehensive metadata** for accurate recommendations

## 🛠️ Customization

### Adding New Movies

1. **Manual Addition**: Edit `data/movies.csv` directly
2. **API Integration**: Use `fetch_tmdb_movies.py` to fetch from TMDB
3. **Custom Sources**: Extend the data collection script for other APIs

### Modifying AI Behavior

- **Prompt Templates**: Edit `backend/PromptTemplate.py` for different AI personalities
- **Embedding Models**: Change models in `backend/Embedding.py`
- **Search Parameters**: Adjust similarity search in `backend/VectorDB.py`

### UI Customization

- **Styling**: Modify CSS in `frontend/app.py`
- **Layout**: Adjust Streamlit components and layout
- **Features**: Add new interactive elements

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Google Gemini AI** for powerful language model capabilities
- **TMDB** for comprehensive movie data
- **Streamlit** for the beautiful web interface
- **FAISS** for efficient vector similarity search
- **SentenceTransformers** for semantic text understanding

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/divyanshsharma2003/Movie-Rec-Model/issues) page
2. Create a new issue with detailed information
3. Include error messages and system information

---

**Made with ❤️ using cutting-edge AI technology** 