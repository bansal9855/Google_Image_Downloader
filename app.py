from flask import Flask, render_template, request, redirect, url_for, flash
import subprocess
import os
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')  

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Extract form data
    keyword = request.form['keyword']
    num_images = request.form['num_images']
    output_folder = request.form['output_folder']
    email = request.form['email']

    
    if not keyword or not num_images.isdigit() or not output_folder or not email:
        flash("Please fill out all fields correctly.", "error")
        return redirect(url_for('form'))

    try:
        
        subprocess.run(['python', 'main.py', keyword, num_images, output_folder, email], check=True)
        flash("Images downloaded, zipped, and emailed successfully!", "success")

    except subprocess.CalledProcessError as e:
        flash(f"An error occurred during processing: {e}", "error")
    except Exception as e:
        flash(f"An unexpected error occurred: {e}", "error")

    return redirect(url_for('form'))

if __name__ == '__main__':
    app.run(debug=True)
