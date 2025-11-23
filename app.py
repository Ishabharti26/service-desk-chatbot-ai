from flask import Flask, render_template, request, jsonify
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
import mysql.connector

app = Flask(__name__)

# Load vector DB
embeddings = OpenAIEmbeddings()
db = FAISS.load_local("embeddings")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="servicedesk"
)
cursor = conn.cursor()

llm = OpenAI(model="gpt-4o-mini")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["msg"]

    # Search knowledge base
    docs = db.similarity_search(user_input, k=2)
    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    You are an IT Support Assistant.
    Use the context below to answer user queries.
    Context: {context}

    User: {user_input}
    """
    bot_reply = llm(prompt)

    # Create ticket
    if "create ticket" in user_input.lower():
        email = "user@gmail.com"
        issue = user_input
        cursor.execute("INSERT INTO tickets(user_email, issue) VALUES(%s, %s)", (email, issue))
        conn.commit()
        bot_reply += "\n\nYour support ticket has been created successfully."

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
   
