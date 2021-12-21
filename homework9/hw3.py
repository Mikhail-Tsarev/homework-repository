import os
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    """
    Counts lines in all files with that extension
    if there are no tokenizer. If a tokenizer is not none,
    it will count tokens.

    :param dir_path: Directory for search
    :param file_extension: File extension
    :param tokenizer: Tokenizer function (Optional)
    :return: Number of lines or tokens
    """

    counter = 0

    for file in os.listdir(dir_path):
        if file.endswith(f".{file_extension}"):
            with open(f"{dir_path}/{file}") as f:

                if not tokenizer:
                    counter += sum(1 for _ in f)
                else:
                    for line in map(tokenizer, f):
                        counter += len(line)
    return counter
