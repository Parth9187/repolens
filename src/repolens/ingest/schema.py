from pydantic import BaseModel


class Chunk(BaseModel):
    chunk_id: str
    repo_name: str
    file_path: str
    symbol_name: str | None
    symbol_type: str
    start_line: int
    end_line: int
    text: str
