from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import get_chatbot_response
from recommend_college import recommend_college
from recommend_branch import recommend_by_branch
import re

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"].lower()

    # detect marks automatically
    marks_match = re.search(r'\b\d{2}\b', user_message)

    # detect branch keywords
    branches = ["cse", "computer", "ai", "artificial intelligence",
                "mechanical", "civil", "electrical"]

    branch_found = None
    for branch in branches:
        if branch in user_message:
            branch_found = branch
            break

    # if both branch and marks present
    if marks_match and branch_found:
        marks = marks_match.group()
        college_rec = recommend_college(marks)
        branch_rec = recommend_by_branch(branch_found)

        reply = f"{branch_rec}\n\n{college_rec}"

    # if only marks present
    elif marks_match:
        marks = marks_match.group()
        reply = recommend_college(marks)

    # if only branch present
    elif branch_found:
        reply = recommend_by_branch(branch_found)

    else:
        reply = get_chatbot_response(user_message)

    return jsonify({"reply": reply})


@app.route("/")
def home():
    return "AI College Assistant Backend Running"


if __name__ == "__main__":
    app.run()