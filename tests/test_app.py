from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    response = client.post("/activities/Chess Club/signup?email=student@mergington.edu")
    assert response.status_code == 200

    unregister_response = client.delete(
        "/activities/Chess Club/unregister?email=student@mergington.edu"
    )
    assert unregister_response.status_code == 200

    activities_response = client.get("/activities")
    activity_data = activities_response.json()["Chess Club"]
    assert "student@mergington.edu" not in activity_data["participants"]
