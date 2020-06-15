import cProfile

from starlette.testclient import TestClient

from test_starlette import app


prof = cProfile.Profile()
prof.enable()
client = TestClient(app)
response = client.get("/")
prof.dump_stats("stats.prof")