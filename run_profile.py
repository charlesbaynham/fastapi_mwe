import cProfile

from fastapi.testclient import TestClient

from test_api import app


prof = cProfile.Profile()
prof.enable()
client = TestClient(app)
response = client.get("/")
prof.dump_stats("stats.prof")