from pathlib import Path

from repolens.ingest.parse_repo_files import parse_repo_files


def test_parse_repo_files() -> None:
    assert parse_repo_files is not None

    repo_path = Path("tests/fixtures/sample_repo")

    files = parse_repo_files(repo_path=repo_path)
    names = {file.name for file in files}

    assert "auth.py" in names
    assert "config.py" in names

    return None
