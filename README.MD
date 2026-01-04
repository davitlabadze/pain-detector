# Pain Detector MVP

A minimal Pain Point Detector web app that highlights pain points from text and renders them as interactive cards with Markdown support.

## Features

Detects pain categories (Time, Cost, Data, Risk) from user input.

Displays results as interactive cards:

Click a card to expand it.

Markdown text is properly rendered, including code blocks, links, lists, and blockquotes.

Copy button:

Copies the text, score, and pain types to clipboard.

GitHub-style code rendering in Markdown.

## Tech Stack

Frontend: HTML, CSS, Vanilla JS

Markdown: marked.js

Backend: Flask (Python 3.12)

Optional: Bootstrap/Tailwind for styling enhancements

## Project Structure (Flask Example)

```bash
    pain_detector_mvp/
    │
    ├─ app.py # Flask application
    ├─ requirements.txt # Python dependencies
    ├─ templates/
    │ └─ index.html # Main HTML template
    └─ static/
    └─ (optional css/js files)
```

## How to Run Locally

Clone the repo

```bash
git clone
cd pain_detector_mvp
```

Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows
```

Install dependencies

```bash
pip install -r requirements.txt

```

Run Flask app

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Or directly:

```bash
python app.py
```

Open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## How It Works

Flask passes a results list to the template:

```json
    results = [
    {
        "text": "Some sample GitHub PR or discussion text...",
        "score": 2,
        "pain_categories": ["Time pain", "Data pain"]
        },
        ...
    ]
```

Template renders each result as a card:

.card-body stores raw Markdown in data-md

Clicking a card converts Markdown to HTML using marked.parse

Copy button reads data-\* attributes and copies formatted text

## Styling

Cards have light background with shadow

Code blocks have dark background (#111827) with light text (#e5e7eb)

Inline code highlighted with light gray background

Blockquotes styled with blue accent

## Example Usage

Detect pain points in a set of GitHub PR discussions or Slack messages.

Render cards for each message:

Expand/collapse card

Copy text for analysis or sharing

Quickly identify Time, Cost, Data, Risk pain points in your team’s workflow

## Dependencies

Python 3.12+

Flask 3.x

marked.js (CDN included in template)

## Next Steps / Improvements

Save results to database (SQLite/PostgreSQL)

Add pain frequency analysis or charts

Auto-generate SaaS ideas based on detected pains

Add multi-language support (e.g., Georgian, English)

## License

MIT © 2026 David Labadze
