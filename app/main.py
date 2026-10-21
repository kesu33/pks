import sqlite3
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "physics.db"


def get_connection():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS concepts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic TEXT NOT NULL,
                name TEXT NOT NULL UNIQUE,
                description TEXT NOT NULL,
                formula TEXT
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                options TEXT NOT NULL,
                correct_answer TEXT NOT NULL,
                explanation TEXT NOT NULL
            )
        """)

        count = conn.execute(
            "SELECT COUNT(*) FROM concepts"
        ).fetchone()[0]

        if count == 0:
            conn.executemany(
                """INSERT INTO concepts
                   (topic, name, description, formula)
                   VALUES (?, ?, ?, ?)""",
                [
                    (
                        "Mechanics",
                        "Newton's Second Law",
                        "Net force equals mass multiplied by acceleration.",
                        "F = ma",
                    ),
                    (
                        "Mechanics",
                        "Velocity",
                        "Displacement per unit time.",
                        "v = displacement / time",
                    ),
                ],
            )

        count = conn.execute(
            "SELECT COUNT(*) FROM questions"
        ).fetchone()[0]

        if count == 0:
            conn.execute(
                """INSERT INTO questions
                   (question, options, correct_answer, explanation)
                   VALUES (?, ?, ?, ?)""",
                (
                    "A 2 kg object accelerates at 3 m/s^2. "
                    "What is the net force?",
                    '["3 N", "5 N", "6 N", "9 N"]',
                    "6 N",
                    "Newton's second law: F = ma = 2 × 3 = 6 N.",
                ),
            )


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="pks",
    description="A starter API for high-school Physics learning.",
    version="0.1.0",
    lifespan=lifespan,
)


class ConceptCreate(BaseModel):
    topic: str = Field(min_length=1, max_length=100)
    name: str = Field(min_length=1, max_length=150)
    description: str = Field(min_length=1, max_length=2000)
    formula: str | None = Field(default=None, max_length=300)


class AnswerSubmission(BaseModel):
    question_id: int
    answer: str = Field(min_length=1, max_length=500)


@app.get("/")
def home():
    return {
        "project": "pks",
        "version": "0.1.0",
        "status": "running",
        "docs": "/docs",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/concepts")
def list_concepts(topic: str | None = None):
    with get_connection() as conn:
        if topic:
            rows = conn.execute(
                """SELECT id, topic, name, description, formula
                   FROM concepts WHERE topic = ? ORDER BY id""",
                (topic,),
            ).fetchall()
        else:
            rows = conn.execute(
                """SELECT id, topic, name, description, formula
                   FROM concepts ORDER BY id"""
            ).fetchall()

    return [dict(row) for row in rows]


@app.post("/concepts", status_code=201)
def create_concept(concept: ConceptCreate):
    try:
        with get_connection() as conn:
            cursor = conn.execute(
                """INSERT INTO concepts
                   (topic, name, description, formula)
                   VALUES (?, ?, ?, ?)""",
                (
                    concept.topic.strip(),
                    concept.name.strip(),
                    concept.description.strip(),
                    concept.formula,
                ),
            )
            concept_id = cursor.lastrowid
            row = conn.execute(
                """SELECT id, topic, name, description, formula
                   FROM concepts WHERE id = ?""",
                (concept_id,),
            ).fetchone()
            return dict(row)
    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="A concept with this name already exists.",
        )


@app.get("/questions")
def list_questions():
    with get_connection() as conn:
        rows = conn.execute(
            """SELECT id, question, options
               FROM questions ORDER BY id"""
        ).fetchall()

    import json

    return [
        {
            "id": row["id"],
            "question": row["question"],
            "options": json.loads(row["options"]),
        }
        for row in rows
    ]


@app.post("/answer")
def submit_answer(submission: AnswerSubmission):
    with get_connection() as conn:
        row = conn.execute(
            """SELECT correct_answer, explanation
               FROM questions WHERE id = ?""",
            (submission.question_id,),
        ).fetchone()

    if row is None:
        raise HTTPException(status_code=404, detail="Question not found.")

    correct = (
        submission.answer.strip().casefold()
        == row["correct_answer"].strip().casefold()
    )

    return {
        "question_id": submission.question_id,
        "correct": correct,
        "score": 1 if correct else 0,
        "explanation": row["explanation"],
    }
