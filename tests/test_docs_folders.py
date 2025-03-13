import os
import pytest

DOCS_DIR = "docs"

# Ignorar carpetas ocultas como .ipynb_checkpoints
EXCLUDE_DIRS = {".ipynb_checkpoints"}

def is_not_empty(directory):
    """Verifica que un directorio no esté vacío, ignorando carpetas ocultas."""
    for root, dirs, files in os.walk(directory):
        # Ignorar carpetas ocultas
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        files = [f for f in files if not f.startswith('.')]
        
        # Si hay archivos visibles o subdirectorios válidos, no está vacío
        if files or dirs:
            return True
    return False

@pytest.mark.parametrize("folder", [
    os.path.join(DOCS_DIR, "css"),
    os.path.join(DOCS_DIR, "homeworks"),
    os.path.join(DOCS_DIR, "homeworks", "data"),
    os.path.join(DOCS_DIR, "homeworks", "images"),
    os.path.join(DOCS_DIR, "images"),
    os.path.join(DOCS_DIR, "images", "icons"),
    os.path.join(DOCS_DIR, "labs"),
    os.path.join(DOCS_DIR, "labs", "data"),
    os.path.join(DOCS_DIR, "lectures"),
    os.path.join(DOCS_DIR, "lectures", "data_manipulation"),
    os.path.join(DOCS_DIR, "lectures", "data_manipulation", "data"),
    os.path.join(DOCS_DIR, "lectures", "data_manipulation", "images"),
    os.path.join(DOCS_DIR, "lectures", "machine_learning"),
    os.path.join(DOCS_DIR, "lectures", "machine_learning", "images"),
    os.path.join(DOCS_DIR, "lectures", "toolkit"),
    os.path.join(DOCS_DIR, "lectures", "toolkit", "images"),
    os.path.join(DOCS_DIR, "lectures", "visualization"),
    os.path.join(DOCS_DIR, "lectures", "visualization", "data"),
    os.path.join(DOCS_DIR, "lectures", "visualization", "images"),
    os.path.join(DOCS_DIR, "projects"),
])
def test_folder_is_not_empty(folder):
    assert os.path.exists(folder), f"La carpeta '{folder}' no existe."
    assert is_not_empty(folder), f"La carpeta '{folder}' está vacía."
