from flask import Flask

from app import home


def test_base_route():
    app = Flask(__name__)
    home()
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.get_data()
    assert response.status_code == 200