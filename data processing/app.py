from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests, webbrowser
import bs4 as bs
from bs4 import BeautifulSoup
import urllib.request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    google_search = requests.get("https://www.google.com/search?q="+msg+"factcheck")
    soup = BeautifulSoup(google_search.text, 'html.parser')
    search_results = soup.select('.kCrYT a')
    msgr="https://google.com"+search_results[0]
    # Create reply
    resp = MessagingResponse()
    resp.message(msgr)
   

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
