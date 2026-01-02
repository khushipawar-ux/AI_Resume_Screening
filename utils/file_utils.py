"""
File Utilities Module
"""
import os
from pathlib import Path
from typing import List

def ensure_directory(directory: str) -> None:
    """Create directory if it doesn't exist"""
    Path(directory).mkdir(parents=True, exist_ok=True)

def get_file_extension(filename: str) -> str:
    """Get file extension"""
    return os.path.splitext(filename)[1].lower()

def list_files_in_directory(directory: str, extensions: List[str] = None) -> List[str]:
    """List files in directory with optional extension filter"""
    files = []
    for file in os.listdir(directory):
        if extensions is None or get_file_extension(file) in extensions:
            files.append(os.path.join(directory, file))
    return files

def save_uploaded_file(file_content: bytes, destination: str) -> str:
    """Save uploaded file to destination"""
    ensure_directory(os.path.dirname(destination))
    with open(destination, 'wb') as f:
        f.write(file_content)
    return destination
