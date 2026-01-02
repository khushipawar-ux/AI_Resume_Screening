"""
Database Connection Module
"""
import psycopg2
from psycopg2.extras import RealDictCursor
from config.settings import DATABASE_URL
import time

class Database:
    """Database connection manager"""
    
    def __init__(self, database_url: str = DATABASE_URL):
        self.database_url = database_url
        self.conn = None
    
    def get_connection(self):
        """Get database connection with retry logic"""
        if self.conn is None or self.conn.closed:
            try:
                self.conn = psycopg2.connect(self.database_url)
            except psycopg2.OperationalError:
                # Simple retry logic could be added here, but for now just raise
                raise
        return self.conn
    
    def create_tables(self):
        """Create all database tables"""
        conn = self.get_connection()
        with conn.cursor() as cur:
            # Job Descriptions
            cur.execute("""
                CREATE TABLE IF NOT EXISTS job_descriptions (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    description TEXT NOT NULL,
                    requirements TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            
            # Candidates
            cur.execute("""
                CREATE TABLE IF NOT EXISTS candidates (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255),
                    email VARCHAR(255),
                    phone VARCHAR(50),
                    resume_path VARCHAR(500),
                    parsed_data TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    jd_id INTEGER REFERENCES job_descriptions(id) ON DELETE CASCADE
                );
            """)
            
            # Match Scores
            cur.execute("""
                CREATE TABLE IF NOT EXISTS match_scores (
                    id SERIAL PRIMARY KEY,
                    candidate_id INTEGER REFERENCES candidates(id) ON DELETE CASCADE,
                    overall_score FLOAT,
                    skill_score FLOAT,
                    experience_score FLOAT,
                    education_score FLOAT,
                    explanation TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            conn.commit()
    
    def get_db(self):
        """Get database connection (generator for dependency injection)"""
        conn = self.get_connection()
        try:
            yield conn
        except Exception:
            conn.rollback()
            raise
        # Note: We don't close the connection here if we want to reuse it,
        # but in a simple script we might. For FastAPI, we usually let the pool handle it.


# Global database instance
db_instance = Database()

def get_db():
    return db_instance.get_db()
