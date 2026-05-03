from flask import Flask, render_template, request, redirect

app = Flask(__name__)

users = []  # temporary storage

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users.append({'username': username, 'password': password})
        return redirect('/login')
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        for user in users:
            if user['username'] == username and user['password'] == password:
                return redirect('/dashboard')

        return "Invalid credentials"
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)

services = []

@app.route('/add_service', methods=['GET', 'POST'])
def add_service():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        contact = request.form['contact']

        services.append({
            'name': name,
            'category': category,
            'contact': contact
        })

        return redirect('/services')

    return render_template('add_service.html')


@app.route('/services')
def view_services():
    return render_template('services.html', services=services)

# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Pass data to HTML
    return render_template("index.html", message="Hello from Python!")

if __name__ == "__main__":
    app.run(debug=True)
