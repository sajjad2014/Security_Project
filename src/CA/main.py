from flask import Flask

from src.CA.CA_model import CA

if __name__ == '__main__':
    ca = CA()
    app = Flask(__name__)
    app.add_url_rule("/incoming_certificate_request/",
                     endpoint="/incoming_certificate_request/", view_func=ca.incoming_certificate_request,
                     methods=["POST"])

    app.run(host="localhost", port=4000)
