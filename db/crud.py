"""
CRUD Operations Module
"""
from typing import List, Optional, Dict, Any
import psycopg2
from psycopg2.extras import RealDictCursor

class CRUDOperations:
    """Database CRUD operations using raw SQL"""
    
    @staticmethod
    def create_job_description(conn, title: str, description: str, requirements: str = None):
        """Create new job description"""
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                INSERT INTO job_descriptions (title, description, requirements)
                VALUES (%s, %s, %s)
                RETURNING id, title, description, requirements, created_at;
                """,
                (title, description, requirements)
            )
            jd = cur.fetchone()
            conn.commit()
            return jd
    
    @staticmethod
    def create_candidate(conn, name: str, email: str, resume_path: str, jd_id: int):
        """Create new candidate"""
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                INSERT INTO candidates (name, email, resume_path, jd_id)
                VALUES (%s, %s, %s, %s)
                RETURNING id, name, email, resume_path, jd_id, created_at;
                """,
                (name, email, resume_path, jd_id)
            )
            candidate = cur.fetchone()
            conn.commit()
            return candidate
    
    @staticmethod
    def create_match_score(conn, candidate_id: int, overall_score: float, 
                          skill_score: float = None, experience_score: float = None,
                          education_score: float = None, explanation: str = None):
        """Create match score"""
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                INSERT INTO match_scores (candidate_id, overall_score, skill_score, experience_score, education_score, explanation)
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING id, candidate_id, overall_score, skill_score, experience_score, education_score, explanation, created_at;
                """,
                (candidate_id, overall_score, skill_score, experience_score, education_score, explanation)
            )
            score = cur.fetchone()
            conn.commit()
            return score
    
    @staticmethod
    def get_job_description(conn, jd_id: int) -> Optional[Dict[str, Any]]:
        """Get job description by ID"""
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM job_descriptions WHERE id = %s;", (jd_id,))
            return cur.fetchone()

    @staticmethod
    def get_all_job_descriptions(conn) -> List[Dict[str, Any]]:
        """Get all job descriptions"""
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM job_descriptions ORDER BY created_at DESC;")
            return cur.fetchall()

    @staticmethod
    def get_candidates_by_jd(conn, jd_id: int) -> List[Dict[str, Any]]:

        """Get all candidates for a job description"""
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                "SELECT * FROM candidates WHERE jd_id = %s ORDER BY created_at DESC;",
                (jd_id,)
            )
            return cur.fetchall()
    
    @staticmethod
    def get_candidate_with_score(conn, candidate_id: int) -> Optional[Dict[str, Any]]:
        """Get candidate with match scores using a JOIN"""
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                SELECT c.*, ms.overall_score, ms.skill_score, ms.experience_score, ms.education_score, ms.explanation
                FROM candidates c
                LEFT JOIN match_scores ms ON c.id = ms.candidate_id
                WHERE c.id = %s;
                """,
                (candidate_id,)
            )
            return cur.fetchone()

