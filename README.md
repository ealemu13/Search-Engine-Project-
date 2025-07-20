# Search-Engine-Web-Crawler-Project-
## 🔍 Project Description

This project is a full-scale implementation of a web search engine built for academic and professional purposes. It is composed of two main components:

## 🔍 Search Engine Project (Advanced CS/SE Track)

This project implements a **scalable, high-performance search engine** built entirely from scratch—without relying on third-party indexing libraries like Lucene or Elasticsearch. Designed to handle tens of thousands of HTML documents, this system emphasizes algorithmic efficiency, memory-aware design, and real-time retrieval accuracy.

### 📁 Project Structure

- **`indexer.py` – Index Construction**
  - Parses raw HTML from crawled `.json` files
  - Builds a custom **inverted index** with term frequencies and document mappings
  - Boosts token importance from `<title>`, `<h1>`, `<strong>`, etc.
  - Performs **Porter stemming**
  - Writes disk-based index shards and URL-ID mappings
  - Supports external memory constraints through partial file flushing and final merging

- **`query_engine.ipynb` – Baseline Search Interface**
  - Loads and queries inverted index files
  - Accepts **natural language queries** from the command line
  - Computes **TF-IDF scores** and performs Boolean AND retrieval
  - Outputs a ranked list of top-5 results by URL

- **`search_demo.ipynb` – Scalable, Disk-Optimized Query Engine**
  - Uses **on-disk posting lists** and precomputed **offset maps** for random access
  - Implements **cache-aware token loading** to limit memory footprint
  - Rewrites index files by token group (e.g., A–Z) for fast retrieval
  - Achieves average query response time **under 300ms**, suitable for production-scale use

---

This project showcases end-to-end system design, algorithm implementation, and performance engineering—core skills for backend, systems, or infrastructure engineering roles.


---

## 🧱 Technologies Used

- **Python 3.10+**
- **BeautifulSoup4** for HTML parsing
- **NLTK** for stemming and text processing
- **JSON** for document structure
- **Custom I/O** for disk-based storage and indexing

---

## ⚙️ Usage

### 🧱 Inverted Index Builder (Indexer)

This script reads crawled HTML content from JSON files, tokenizes and stems the text, and builds a disk-based inverted index.

**To run:**
```bash
# From the project root or indexer folder
python3 indexer.py
```

### 🔍 Query Engine (TF-IDF Search)

This interactive script loads a disk-based inverted index and allows users to run keyword queries. It uses Boolean AND and TF-IDF scoring to rank and return the top relevant URLs.

**To run:**
```bash
# From the project root or query_engine folder
jupyter notebook query_engine.ipynb
```

### 🚀 Search Engine Demo (Advanced Disk-Based TF-IDF Engine)

This notebook demonstrates a search engine. The system reads JSON files, builds a disk-based inverted index with offset maps, and handles real-time search queries using TF-IDF scoring.
```bash
jupyter notebook search_demo.ipynb
```

### 🤝 Collaborators
Developed in partnership with mynameisnhu and ankazi for the Search Engine project at UC Irvine.


