from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# Response dictionary with predefined questions and answers
responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What can I do for you?",
    "how are you?": "I'm a chatbot, so I'm always good! How about you?",
    "what is your name?": "I'm Chatbot. Nice to meet you!",
    "bye": "Goodbye! Have a great day!",
    "what can you do?": "I can chat with you and help answer basic questions.",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "what is machine learning?": "Machine learning is a field of artificial intelligence that uses statistical techniques to give computer systems the ability to 'learn' from data.",
    "what is nlp?": "NLP stands for Natural Language Processing, a field of artificial intelligence focused on the interaction between computers and humans through natural language.",
    "what is a neural network?": "A neural network is a series of algorithms that attempts to recognize underlying relationships in a set of data through a process that mimics the way the human brain operates.",
    "what is supervised learning?": "Supervised learning is a type of machine learning where the model is trained on labeled data.",
    "what is unsupervised learning?": "Unsupervised learning is a type of machine learning where the model is trained on unlabeled data and has to find patterns and relationships in the data.",
    "what is reinforcement learning?": "Reinforcement learning is a type of machine learning where an agent learns to make decisions by taking actions in an environment to maximize cumulative reward.",
    "what is a decision tree?": "A decision tree is a model used for classification and regression that splits the data into subsets based on the value of input features.",
    "what is random forest?": "Random forest is an ensemble learning method that constructs multiple decision trees and combines their outputs to improve accuracy and reduce overfitting.",
    "what is svm?": "Support Vector Machine (SVM) is a supervised learning model used for classification and regression that finds the hyperplane that best separates the data into classes.",
    "what is k-means clustering?": "K-means clustering is an unsupervised learning algorithm that partitions data into k clusters, where each data point belongs to the cluster with the nearest mean.",
    "what is deep learning?": "Deep learning is a subset of machine learning that uses neural networks with many layers (deep neural networks) to model complex patterns in data.",
    "what is overfitting?": "Overfitting is a modeling error that occurs when a machine learning model captures noise in the training data and performs poorly on new, unseen data.",
    "what is underfitting?": "Underfitting is a modeling error that occurs when a machine learning model is too simple to capture the underlying pattern in the data, resulting in poor performance.",
    "what is two sum?": "Use a hash map to store indices of the numbers.",
    "what is longest substring without repeating characters?": "Use a sliding window with a hash set.",
    "what is merge intervals?": "Sort the intervals and merge overlapping ones.",
    "what is linked list cycle?": "Use two pointers (slow and fast) to detect a cycle.",
    "what is valid parentheses?": "Use a stack to check for matching pairs.",
    "what is maximum subarray?": "Use Kadane's algorithm.",
    "what is climbing stairs?": "Use dynamic programming to find the number of ways.",
    "what is binary tree inorder traversal?": "Use a stack to simulate recursion iteratively.",
    "what is maximum depth of binary tree?": "Use recursion or an iterative approach with a stack or queue.",
    "what is palindrome linked list?": "Use two pointers to find the middle and then reverse the second half."
}

def levenshtein_distance(s1, s2):
    """
    Computes the Levenshtein distance between two strings.

    Args:
        s1 (str): The first string.
        s2 (str): The second string.

    Returns:
        int: The Levenshtein distance between the two strings.
    """
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def get_closest_response(user_input):
    """
    Finds the closest response based on the user's input.

    Args:
        user_input (str): The user input.

    Returns:
        str: The closest response.
    """
    closest_response = None
    min_distance = float('inf')
    for question in responses:
        distance = levenshtein_distance(user_input.lower(), question)
        if distance < min_distance:
            min_distance = distance
            closest_response = responses[question]
    return closest_response

@app.route("/")
def home():
    """
    Renders the homepage.

    Returns:
        str: The rendered HTML template for the homepage.
    """
    return render_template("index.html")

@app.route("/get", methods=["GET", "POST"])
def chat_response():
    """
    Gets the chatbot response for the user input.

    Returns:
        str: The chatbot's response in JSON format.
    """
    user_input = request.args.get('msg')
    response = get_closest_response(user_input)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
