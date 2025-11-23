#  Intelligent Service Desk Chatbot (AI + Automation)

An AI-powered Service Desk Chatbot that answers FAQs, resets passwords, troubleshoots issues, and creates support tickets using AI + RAG.

---

##  Features
- LLM-powered chatbot
- RAG-based knowledge retrieval (FAISS)
- MySQL ticket creation
- Flask backend
- Simple HTML/CSS chat interface

---

##  Tech Stack
- Python  
- Flask  
- OpenAI API  
- LangChain  
- FAISS  
- MySQL  
- HTML/CSS/JavaScript  

---

##  Setup Instructions

### 1️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 2️⃣ Create MySQL Database


```
CREATE DATABASE servicedesk;
USE servicedesk;
```

### 3️⃣ Create Tickets Table

```
CREATE TABLE tickets (
id INT AUTO_INCREMENT PRIMARY KEY,
user_email VARCHAR(100),
issue TEXT,
status VARCHAR(20) DEFAULT 'Open',
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 4️⃣ Generate Embeddings

```
python generate_embeddings.py
```

### 5️⃣ Run the Flask App

```
python app.py
```

---

##  Sample Queries
- "How do I reset my password?"
- "Create ticket for VPN issue."
- "How to check ticket status?"

---

##  Future Improvements
- Deploy on AWS / Azure  
- Add authentication  
- Add more IT troubleshooting flows  
- Integrate with ServiceNow or Jira APIs  




