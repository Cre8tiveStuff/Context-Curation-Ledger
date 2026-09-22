import sqlite3
from datetime import datetime

COMPARISON_DB = "comparison_log.db"


def init_comparison_db():
    conn = sqlite3.connect(COMPARISON_DB)
    conn.execute("""CREATE TABLE IF NOT EXISTS comparisons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        question TEXT,
        baseline_answer TEXT,
        baseline_score REAL,
        curated_answer TEXT,
        curated_score REAL
    )""")
    conn.commit()
    conn.close()


def log_comparison(question, baseline_answer, baseline_score, curated_answer, curated_score):
    init_comparison_db()
    conn = sqlite3.connect(COMPARISON_DB)
    conn.execute(
        "INSERT INTO comparisons (timestamp, question, baseline_answer, baseline_score, curated_answer, curated_score) VALUES (?, ?, ?, ?, ?, ?)",
        (datetime.now().isoformat(), question, baseline_answer, baseline_score, curated_answer, curated_score)
    )
    conn.commit()
    conn.close()


def get_comparisons():
    conn = sqlite3.connect(COMPARISON_DB)
    rows = conn.execute("SELECT question, baseline_score, curated_score FROM comparisons").fetchall()
    conn.close()
    return rows