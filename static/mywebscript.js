
let RunSentimentAnalysis = () => {
    const textToAnalyze = document.getElementById("textToAnalyze").value;
    const responseElement = document.getElementById("system_response");

    if (!textToAnalyze.trim()) {
        responseElement.textContent = "Please enter text to analyze.";
        return;
    }

    const xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState === 4) {
            responseElement.textContent = this.responseText;
        }
    };

    xhttp.open(
        "GET",
        "/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze),
        true
    );

    xhttp.send();
};
