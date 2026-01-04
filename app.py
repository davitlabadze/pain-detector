from flask import Flask, render_template, jsonify
from scraper import get_texts
from pain_detector import detect_pain

app = Flask(__name__)

@app.route('/')
def dashboard():
    texts = get_texts()
    pain_results = detect_pain(texts)
    return render_template('dashboard.html', results=pain_results)

@app.route('/api/pain')
def pain_api():
    texts = get_texts()
    pain_results = detect_pain(texts)
    return jsonify(pain_results)

if __name__ == '__main__':
    app.run(debug=True)
