import server
import pytest
from threading import Thread


@pytest.fixture(scope='session', autouse=True)
def server_setup():
    instance = server.create_server()
    process = Thread(target=instance.serve_forever)
    process.setDaemon(True)
    process.start()
