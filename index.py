from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML Template for the Login Page
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        .message {
            margin-top: 20px;
            font-size: 18px;
        }
        .success {
            color: green;
        }
        .error {
            color: red;
        }
        input, button {
            display: block;
            margin: 10px auto;
            padding: 10px;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <h2>LOGIN</h2>
    {% if message %}
        <p class="message {{ 'success' if success else 'error' }}">{{ message }}</p>
    {% endif %}
    <form method="post">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Login</button>
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    message = None
    success = False
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Simulated insecure logic
        if username == "admin" and password == "admin":
            message = "Login successful!"
            success = True
        elif "'" in username or "'" in password:
            # Simulate an SQL injection pattern success
            message = "Login successful! Flag: M1tMCTF{SQL_INJECTION_101}"
            success = True
        else:
            message = "Invalid username or password."

    return render_template_string(html_template, message=message, success=success)

if __name__ == "__main__":
    app.run(debug=True)
