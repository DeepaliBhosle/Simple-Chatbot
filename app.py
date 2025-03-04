from flask import Flask, request, render_template
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

app = Flask(__name__)

key = "your-text-analytics-key"
endpoint = "your-text-analytics-endpoint"

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    documents = [text]
    response = client.analyze_sentiment(documents=documents)[0]
    sentiment = response.sentiment
    return render_template('result.html', sentiment=sentiment)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
