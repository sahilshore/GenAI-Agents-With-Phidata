## 📦 Agents Included

### 1️ Finance Agent
- Fetches real-time stock prices  
- Provides analyst recommendations  
- Retrieves company information and latest news  

**Tools Used:** YFinance  

---

### 2️ Hacker News Agent
- Fetches trending technology stories  
- Summarizes top Hacker News posts  
- Answers follow-up questions about news  

**Tools Used:** Hacker News API  

---

### 3️ Movie Data Agent
- Analyzes the IMDb Top 1000 movies dataset  
- Automatically generates SQL queries from natural language  
- Uses DuckDB for fast local analytics  

**Data Source:** IMDb CSV  
**Database:** DuckDB  

---

### 4️ RAG (Retrieval-Augmented Generation) Agent
- Reads and indexes PDF documents  
- Stores embeddings using pgvector  
- Retrieves relevant context before answering queries  

**Knowledge Source:** PDF documents  
**Vector Database:** PostgreSQL + pgvector  

---

### 5️ Instructions Agent
- Uses role-based prompting  
- Generates creative short stories  
- Produces controlled and context-aware content  

---

## 🔌 LLM Providers

This project supports multiple LLM backends:

- **Groq (Default):** Fast, free-tier friendly, low-latency inference  
- **OpenAI (Optional):** Higher-quality responses suitable for production use  

Switching between providers requires only configuration changes.

---

## 🛠️ Technology Stack
- Python  
- Phidata  
- Groq API  
- OpenAI API  
- DuckDB  
- PostgreSQL  
- pgvector  
- RAG (PDF-based retrieval)  

---

## ⚙️ How To Use
1. Clone the repository  
2. Create and activate a virtual environment  
3. Install dependencies from `requirements.txt`  
4. Add required API keys in a `.env` file  
5. Run any agent file individually  

Each agent can be executed independently depending on the use case.

---

## 👨‍💻 Who This Is For

This project is suitable for:
- Students learning Generative AI  
- Developers exploring Agentic AI systems  
- Engineers building RAG or tool-using LLM applications  
- Anyone creating a GenAI-focused portfolio  

---

## ⭐ Final Note

This repository is not about simple prompt engineering.  
It demonstrates how intelligent AI agents **reason, act, retrieve information, and produce reliable outputs** using modern Generative AI tooling.
