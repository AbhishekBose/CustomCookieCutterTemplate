import inspect
import os
import sys

CURRENTDIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
ROOTDIR = os.path.dirname(CURRENTDIR)
APPDIR = os.path.join(ROOTDIR, "app")
sys.path.append(APPDIR)

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
