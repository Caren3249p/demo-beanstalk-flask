from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
    return "Flask funcionando en Elastic Beanstalk - version 1"

@application.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    application.run()