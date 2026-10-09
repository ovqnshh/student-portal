from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

myapp = Flask(__name__)

REQUEST_COUNT = Counter(
    "student_app_request_total",
    "Total number of requests to Student App",
    ["endpoint"]
)

@myapp.route("/home")
def home_page():
    REQUEST_COUNT.labels(endpoint="/home").inc()
    return "<h1>This is a Kubernetes Flask based application</h1>"

@myapp.route("/about")
def about_us():
    REQUEST_COUNT.labels(endpoint="/about").inc()
    return "<h1>This is my About Us Page</h1>"

@myapp.route("/services")
def services():
    REQUEST_COUNT.labels(endpoint="/services").inc()
    return "<h1>This is my Services Page</h1>"

@myapp.route("/contact")
def contact():
    REQUEST_COUNT.labels(endpoint="/contact").inc()
    return "<h1>This is my Contact Us Page</h1>"

@myapp.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    myapp.run("0.0.0.0", port=5000)
