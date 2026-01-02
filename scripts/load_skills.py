"""
Script to Load Skills Taxonomy
"""
import json
from pathlib import Path

def load_skills_taxonomy():
    """Load skills taxonomy from JSON file"""
    skills_file = Path(__file__).parent.parent / "data" / "skill_taxonomy" / "skills.json"
    
    with open(skills_file, 'r') as f:
        skills_data = json.load(f)
    
    print(f"Loaded {len(skills_data)} skill categories")
    return skills_data

if __name__ == "__main__":
    skills = load_skills_taxonomy()
    print(json.dumps(skills, indent=2))
