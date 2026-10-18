
"""Flask web application for emotion detection."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the home page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze text and return the emotion results."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        return "Invalid text! Please enter text to analyze.", 400

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Emotion service is unavailable. Please try again later.", 503

    return f"For the given statement, the system response is {result}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
