"""
File operations tools with sandbox security restrictions.
"""
import os
from pathlib import Path
from typing import List, Optional

SANDBOX_DIR = Path("sandbox")

def validate_sandbox(path: str) -> bool:
    """
    Ensure the path is within the sandbox directory.
    Security: Prevents agents from writing outside designated area.
    
    Args:
        path: File path to validate
        
    Returns:
        bool: True if path is safe, False otherwise
    """
    try:
        abs_path = Path(path).resolve()
        abs_sandbox = SANDBOX_DIR.resolve()
        return abs_sandbox in abs_path.parents or abs_path == abs_sandbox
    except Exception:
        return False

def read_file(path: str) -> Optional[str]:
    """
    Read content from a file.
    
    Args:
        path: Path to the file
        
    Returns:
        str: File content or None if error
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"❌ Error reading {path}: {e}")
        return None

def write_file(path: str, content: str) -> bool:
    """
    Write content to a file (sandbox restricted).
    
    Args:
        path: Path to the file
        content: Content to write
        
    Returns:
        bool: True if successful, False otherwise
    """
    if not validate_sandbox(path):
        print(f"⚠️ Security: Attempted write outside sandbox: {path}")
        return False
    
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"❌ Error writing {path}: {e}")
        return False

def list_python_files(directory: str) -> List[str]:
    """
    List all Python files in a directory recursively.
    
    Args:
        directory: Directory to search
        
    Returns:
        List[str]: List of Python file paths
    """
    python_files = []
    try:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.py'):
                    python_files.append(os.path.join(root, file))
    except Exception as e:
        print(f"❌ Error listing files in {directory}: {e}")
    
    return python_files

def copy_to_sandbox(source_dir: str, target_name: str = "working") -> str:
    """
    Copy source directory to sandbox for safe processing.
    
    Args:
        source_dir: Source directory path
        target_name: Name for sandbox subdirectory
        
    Returns:
        str: Path to sandbox copy
    """
    import shutil
    
    sandbox_path = SANDBOX_DIR / target_name
    
    # Clean existing sandbox
    if sandbox_path.exists():
        shutil.rmtree(sandbox_path)
    
    # Copy to sandbox
    try:
        shutil.copytree(source_dir, sandbox_path)
        print(f"✅ Copied {source_dir} to {sandbox_path}")
        return str(sandbox_path)
    except Exception as e:
        print(f"❌ Error copying to sandbox: {e}")
        return source_dir
