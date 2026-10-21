from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_sample_concepts_exist():
    response = client.get("/concepts")
    assert response.status_code == 200
    names = [item["name"] for item in response.json()]
    assert "Newton's Second Law" in names


def test_sample_question_and_correct_answer():
    response = client.get("/questions")
    assert response.status_code == 200
    questions = response.json()
    assert len(questions) >= 1

    question = questions[0]
    result = client.post(
        "/answer",
        json={"question_id": question["id"], "answer": "6 N"},
    )
    assert result.status_code == 200
    assert result.json()["correct"] is True


def test_unknown_question_returns_404():
    response = client.post(
        "/answer",
        json={"question_id": 999999, "answer": "6 N"},
    )
    assert response.status_code == 404


def test_create_concept():
    response = client.post(
        "/concepts",
        json={
            "topic": "Thermodynamics",
            "name": "Starter Test Concept",
            "description": "A test concept.",
            "formula": "Q = mcΔT",
        },
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Starter Test Concept"
