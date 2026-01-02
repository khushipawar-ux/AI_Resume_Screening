"""
Database Migration Script
"""
from pathlib import Path
import sys

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from db.database import Database

def migrate_database():
    """Create database tables"""
    print("Creating database tables...")
    
    db = Database()
    db.create_tables()
    
    print("Database tables created successfully!")

if __name__ == "__main__":
    migrate_database()
