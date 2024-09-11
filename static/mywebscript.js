let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }
    };
    
    xhttp.open("POST", "/emotionDetector", true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    
    // Sending the text to analyze as JSON in the request body
    xhttp.send(JSON.stringify({ text: textToAnalyze }));
}
