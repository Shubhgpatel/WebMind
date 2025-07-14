# 💬 RAG-Powered Website Chatbot

A full-stack, real-time chatbot application that leverages Retrieval-Augmented Generation (RAG) with LangChain and LLaMA 3 to provide accurate, source-backed answers from live website content.

## 🚀 Features

- **🔍 Web Crawling & Scraping**: Fetches and cleans content from entire websites using rotating proxies
- **🧠 Retrieval-Augmented Generation**: Employs a LLaMA 3 model integrated via LangChain to provide context-aware answers
- **📦 Vector Store with Qdrant**: Stores document embeddings for efficient and scalable retrieval
- **💬 Streamlit Chat UI**: Intuitive, real-time interface with chat history, user roles, and persistent sessions
- **🔄 Dynamic Content Reloading**: Supports both new and previously cached websites
- **🗃 Chat History Tracking**: Logs interactions in a SQLite database for future reference

## 🛠 Architecture

```
User ↔ Streamlit UI ↔ LangChain QA Chain ↔ Qdrant Vector Store ↔ Web Scraping Pipeline
```

## 📁 Project Structure

```
rag-chatbot/
├── app.py                    # Main Streamlit app with session management and chat UI
├── web_crawler.py           # Crawls and collects internal URLs
├── web_scraper.py           # Scrapes HTML content and converts it to markdown
├── vector_store.py          # Handles embedding creation and Qdrant vector store integration
├── rag_system.py            # Sets up LangChain RAG chain using LLaMA 3 with custom prompts
├── chat_history_db.py       # Manages chat and website metadata persistence via SQLite
├── ui_components.py         # Handles all UI/UX components using Streamlit
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (not tracked in git)
├── data/
│   ├── scraped_data/        # Processed documents storage
│   └── crawled_urls.txt     # Tracked URLs
└── chat_history.db          # SQLite database for chat history
```

## 📦 Installation

### Prerequisites

- Python 3.8+
- Active internet connection
- API keys for required services

### Environment Variables

Create a `.env` file in the project root with the following variables:

```bash
GROQ_API_KEY=your_groq_key_here
QDRANT_URL=https://your-qdrant-instance-url
QDRANT_API_KEY=your_qdrant_api_key_here
```

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/rag-chatbot.git
   cd rag-chatbot
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your actual API keys
   ```

5. **Initialize data directories**
   ```bash
   mkdir -p data/scraped_data
   ```

## 🚦 Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Access the web interface**
   - Open your browser and navigate to `http://localhost:8501`

3. **Using the chatbot**
   - Enter a website URL in the sidebar
   - Wait for the system to crawl, scrape, and index the content
   - Start asking questions about the website content
   - View source-backed answers with references

## 🧪 Technologies

| Component | Technology |
|-----------|------------|
| **LLM Framework** | LangChain |
| **Language Model** | LLaMA 3 (via GROQ API) |
| **Vector Database** | Qdrant |
| **Web Interface** | Streamlit |
| **Database** | SQLite |
| **Web Scraping** | BeautifulSoup |
| **Content Processing** | html2text |
| **HTTP Requests** | requests |

## 📊 System Requirements

- **Memory**: Minimum 4GB RAM (8GB recommended)
- **Storage**: 1GB free space for data storage
- **Network**: Stable internet connection for API calls and web scraping

## 🔧 Configuration

### Customizing the RAG System

Edit `rag_system.py` to modify:
- Prompt templates
- Retrieval parameters
- Model settings

### Adjusting Scraping Behavior

Modify `web_scraper.py` to:
- Change content filtering rules
- Adjust scraping delays
- Configure proxy rotation

### Vector Store Configuration

Update `vector_store.py` for:
- Embedding model selection
- Qdrant collection settings
- Similarity search parameters

## 📈 Performance Tips

1. **Optimize Vector Store**: Use appropriate embedding dimensions for your use case
2. **Efficient Scraping**: Implement rate limiting to avoid being blocked
3. **Caching**: Leverage Streamlit's caching for better performance
4. **Batch Processing**: Process multiple URLs in batches when possible

## 🔒 Security Considerations

- Store API keys securely in environment variables
- Implement rate limiting for API calls
- Validate and sanitize user inputs
- Use HTTPS for all external API calls

## 🐛 Troubleshooting

### Common Issues

1. **API Key Errors**
   - Verify your API keys in the `.env` file
   - Check API key permissions and quotas

2. **Vector Store Connection Issues**
   - Ensure Qdrant instance is running and accessible
   - Check network connectivity and firewall settings

3. **Web Scraping Failures**
   - Some websites block automated scraping
   - Try using different user agents or proxies

4. **Memory Issues**
   - Reduce batch sizes for large websites
   - Clear vector store periodically

### Debug Mode

Enable debug logging by setting:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
