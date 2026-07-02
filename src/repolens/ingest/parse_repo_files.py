from collections.abc import Iterator
from pathlib import Path

IGNORE_DIRS = {".git", ".venv", "venv", "__pycache__", "node_modules", "build", "dist"}


def parse_repo_files(repo_path: Path) -> Iterator[Path]:
    for root, dirs, files in repo_path.walk(top_down=True, follow_symlinks=False):
        dirs[:] = [dir for dir in dirs if dir not in IGNORE_DIRS]

        for file in files:
            if file.endswith(".py"):
                yield root / file
