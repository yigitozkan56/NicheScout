import os
import tempfile

from fastapi.testclient import TestClient

from app import NicheScoutDB, score_niche_opportunity, web_app


def test_score_niche_opportunity():
    sample = {
        "niche_id": "test-niche",
        "topic": "Automated Webhook Debugger",
        "discussion_snippet": "I am tired of manually testing webhooks. Is there a tool that replays payloads?",
        "trend_volume": 80,
        "community_upvotes": 200,
    }
    scored = score_niche_opportunity(sample)
    assert scored["pain_signal_hits"] == 2
    assert scored["validation_score"] >= 80.0


def test_niche_db_and_api():
    with tempfile.TemporaryDirectory() as tmpdir:
        db = NicheScoutDB(db_path=os.path.join(tmpdir, "niche.db"))
        items = db.list_niches(min_score=60.0)
        assert len(items) >= 2

    client = TestClient(web_app)
    resp = client.get("/api/niches")
    assert resp.status_code == 200
    assert resp.json()["count"] >= 3
