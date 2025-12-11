from typing import List, Tuple


def read_file_as_lines(file_path: str) -> List[str]:
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]


def read_single_line(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.readline().strip()


def read_several_parts(file_path: str) -> List[List[str]]:
    parts = []
    current_part = []

    with open(
        file_path,
        "r",
    ) as f:
        for line in f:
            stripped_line = line.strip()
            if stripped_line:
                current_part.append(stripped_line)
            elif current_part:
                parts.append(current_part)
                current_part = []
        if current_part:
            parts.append(current_part)

    return parts
