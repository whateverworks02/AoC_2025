from typing import List, Tuple


def read_file_as_lines(file_path: str) -> List[str]:
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]


def read_single_line(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.readline().strip()
