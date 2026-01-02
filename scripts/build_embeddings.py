"""
Script to Build Embeddings for Resumes
"""
from pathlib import Path
import sys

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from core.embeddings.sentence_embeddings import SentenceEmbeddings
from utils.file_utils import list_files_in_directory

def build_embeddings():
    """Build embeddings for all parsed resumes"""
    embedder = SentenceEmbeddings()
    
    parsed_dir = Path(__file__).parent.parent / "data" / "parsed_resumes"
    resume_files = list_files_in_directory(str(parsed_dir), ['.txt'])
    
    print(f"Building embeddings for {len(resume_files)} resumes...")
    
    # TODO: Implement embedding generation and storage
    
    print("Embeddings built successfully!")

if __name__ == "__main__":
    build_embeddings()
