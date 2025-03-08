from flask import Flask, request, render_template

app = Flask(__name__)

# Simulated database of users
users = [
    {"username": "admin", "password": "admin123"},
    {"username": "user", "password": "user123"}
]

@app.route("/")
def home():
    # Serve the HTML form
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # Simulate a vulnerable SQL query
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"Executing query: {query}")  # Simulate query execution

    # Simulate the database response
    # If the query is always true (e.g., due to SQL injection), return success
    if "OR '1'='1" in query:
        return "<h1 class='text-center mt-5'>Bienvenue, Admin !</h1>"
    
    # Check if the user exists in the simulated database
    for user in users:
        if user["username"] == username and user["password"] == password:
            return f"<h1 class='text-center mt-5'>Bienvenue, {username} !</h1>"
    
    return "<h1 class='text-center mt-5'>Échec de la connexion. Nom d'utilisateur ou mot de passe invalide.</h1>"

if __name__ == "__main__":
    app.run(debug=True)