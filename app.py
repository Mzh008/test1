"""Simple Flask app wiring the CampusAgent."""

from flask import Flask, render_template, request, jsonify, redirect

from campus_ai import CampusAgent
from campus_ai.plugins.rag import RAGPlugin
from campus_ai.plugins.gpa import GPACalculatorPlugin
from campus_ai.plugins.research import ResearchPlugin
from campus_ai.plugins.websearch import WebSearchPlugin
from campus_ai.knowledge_base.in_memory import InMemoryKnowledgeBase

app = Flask(__name__)

# Example setup
kb = InMemoryKnowledgeBase([
    "The library closes at 10pm.",
    "Final exams are scheduled for the first week of May.",
])

agent = CampusAgent()
agent.plugins = {
    "rag": RAGPlugin(kb),
    "gpa": GPACalculatorPlugin(),
    "research": ResearchPlugin(),
    "websearch": WebSearchPlugin(),
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Placeholder: accept any credentials
        return redirect("/")
    return render_template("login.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    # For demo purposes, we simply echo back the tool list
    if message.startswith("/"):
        tool, *rest = message[1:].split()
        try:
            result = agent.run_tool(tool, query=" ".join(rest))
        except Exception as exc:
            result = str(exc)
    else:
        result = f"Echo: {message}"
    return jsonify({"reply": result})


if __name__ == "__main__":
    app.run(debug=True)
