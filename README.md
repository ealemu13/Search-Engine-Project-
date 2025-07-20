# Search-Engine-Web-Crawler-Project-
# 🕵️‍♂️ Search Engine from Scratch

A high-performance, disk-based search engine built from the ground up in Python, capable of indexing and querying tens of thousands of web pages under strict runtime and memory constraints.

> ✅ Completed the advanced **Algorithms and Data Structures Developer** version  
> 📁 Indexed over 56,000 ICS subdomain web pages  
> 🚀 Achieved sub-300ms query response time  
> 🧠 Built entirely without the use of search libraries like ElasticSearch or Lucene

---

## 🔍 Project Description

This project is a full-scale implementation of a web search engine built for academic and professional purposes. It is composed of two main components:

### 1. **Web Crawler**
A distributed crawler built on top of the [spacetime-crawler4py](https://github.com/Mondego/spacetime-crawler4py) framework, enhanced to:
- Respect robots.txt and politeness rules
- Extract and defragment URLs
- Parse and persist the content of web pages
- Identify and avoid crawler traps, low-information pages, and duplicate content
- Generate analytics reports (e.g., most common words, subdomain distributions)

### 2. **Search Engine**
Built with a modular, milestone-driven approach:
- **Indexer**
  - Implements a custom inverted index using disk-based partial indexing
  - Supports multiple merges of on-disk index shards
  - Applies stemming (Porter) and HTML parsing with tag-weighting
  - Boosts term weight for important tags (e.g., `<title>`, `<h1>`, `<strong>`)
- **Query Engine**
  - Accepts natural-language queries via a console interface
  - Uses tf-idf ranking and tag boosting for scoring
  - Loads only necessary postings from disk at query time (efficient memory use)
  - Produces ranked results by URL within 300ms average response time

---

## 📦 Features

- ✅ Inverted Index Construction with Stemming
- ✅ Partial Index Merging and Disk-Based Storage
- ✅ Tf-idf Based Ranking with Tag Importance
- ✅ Duplicate and Near-Duplicate Page Detection
- ✅ Word Position Tracking (Positional Indexing)
- ✅ Support for 2-gram/3-gram Token Matching *(extra credit)*
- ✅ Web crawler analytics: subdomain counts, word frequency, longest page
- ✅ Designed for large-scale document retrieval (56k+ documents)

---

## 🧱 Technologies Used

- **Python 3.10+**
- **BeautifulSoup4** for HTML parsing
- **NLTK** for stemming and text processing
- **JSON** for document structure
- **Custom I/O** for disk-based storage and indexing

---

## ⚙️ Usage

### 🕸️ Crawler
```bash
cd crawler/
python3 main.py
