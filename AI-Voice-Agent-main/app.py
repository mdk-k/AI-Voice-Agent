from flask import Flask
from routes.twilio_webhook import twilio_bp

app = Flask(__name__)
app.register_blueprint(twilio_bp, url_prefix='/twilio')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
