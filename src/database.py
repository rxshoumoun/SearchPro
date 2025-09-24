import sqlite3
from datetime import datetime
import os

class Database:
    def __init__(self, db_path="research_cache.db"):
        self.db_path = db_path
        # Create database directory if it doesn't exist
        os.makedirs(os.path.dirname(os.path.abspath(db_path)) if os.path.dirname(db_path) else '.', exist_ok=True)
        self.init_db()

    def init_db(self):
        """Initialize database with required tables"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS research_cache (
                    id INTEGER PRIMARY KEY,
                    topic TEXT NOT NULL,
                    report TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            # Add index for faster topic searches
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_topic 
                ON research_cache(topic)
            """)
            conn.commit()

    def cache_research(self, topic: str, report: str):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO research_cache (topic, report) VALUES (?, ?)",
                (topic, report)
            )
            conn.commit()

    def get_recent_research(self, limit: int = 10) -> list:
        with sqlite3.connect(self.db_path) as conn:
            result = conn.execute(
                "SELECT topic, report, created_at FROM research_cache ORDER BY created_at DESC LIMIT ?",
                (limit,)
            )
            return [{"topic": row[0], "report": row[1], "date": row[2]} for row in result]