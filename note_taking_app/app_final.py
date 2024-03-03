from flask import Flask, render_template, request, session, redirect
import secrets  # Import for secure session key generation

app = Flask(__name__)

# Set a secure secret key (replace with a strong random value)
app.secret_key = secrets.token_bytes(32)  # Recommended for production
# app.secret_key = 'your_secure_secret_key'  # Replace with your own key for development only

@app.route('/', methods=["GET", "POST"])
def index():
    global notes
    notes = session.get('notes', [])
    
    if request.method == "POST":
        note = request.form.get("note")
        if note:  # Validate if note is not empty
            notes.append(note)
            session['notes'] = notes  # Store notes in session
        return redirect('/')  # Redirect to avoid duplicate form submissions

    # Retrieve notes from session or initialize an empty list if not found
    return render_template("sample.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
