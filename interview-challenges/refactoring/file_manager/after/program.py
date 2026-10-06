import json
from pathlib import Path

import pytest


class IdFinder:
    def __init__(self, file_name: str, dir_name: str, file_extension: str):
        self.file_path = Path(dir_name) / f"{file_name}.{file_extension}"
        self.numbers = load_integers(self.file_path)

    def contains(self, id: int) -> bool:
        return id in self.numbers


def load_integers(file_path: Path) -> list[int]:
    if not file_path.is_file():
        raise FileNotFoundError(f"File {file_path} does not exist.")
    match file_path.suffix:
        case ".txt":
            return load_integers_from_text_file(file_path)
        case ".json":
            return load_integers_from_json_file(file_path)
        case _:
            raise ValueError(f"File suffix {file_path.suffix} is not supported.")


def load_integers_from_json_file(file_path: Path) -> list[int]:
    with open(file_path, "r") as f:
        return json.load(f)


def load_integers_from_text_file(file_path: Path) -> list[int]:
    with open(file_path, "r") as f:
        content = f.read()
    return [int(num) for num in content.split(",")]


class TestIdFinder:
    @pytest.fixture
    def txt_file_with_numbers(self, tmpdir: str) -> Path:
        file_path = Path(tmpdir) / "test_file.txt"
        with open(file_path, "w") as f:
            f.write("1,2,3,4,5")
        return file_path

    @pytest.fixture
    def json_file_with_numbers(self, tmpdir: str) -> Path:
        file_path = Path(tmpdir) / "test_file.json"
        with open(file_path, "w") as f:
            json.dump(f, [1,2,3,5])
        return file_path

    @pytest.mark.parametrize("search_for,expected", ((1, True), (50, False)))
    def test_contains_should_return_correct_result_with_txt_file(
        self, txt_file_with_numbers, tmpdir: str, search_for: int, expected: bool
    ):
        finder = IdFinder("test_file", tmpdir, "txt")
        assert finder.contains(search_for) == expected


    @pytest.mark.parametrize("search_for,expected", ((1, True), (50, False)))
    def test_contains_should_return_correct_result_with_json_file(
        self, json_file_with_numbers, tmpdir: str, search_for: int, expected: bool
    ):
        finder = IdFinder("test_file", tmpdir, "json")
        assert finder.contains(search_for) == expected


class TestLoadIntegers:
    def test_should_raise_filenotfounderror_if_file_does_not_exist(self):
        file_path = Path("./some_path_that_does_not_exist")
        match_message = f"File {file_path} does not exist"
        with pytest.raises(FileNotFoundError, match=match_message):
            load_integers(file_path)

    def test_should_load_integers_from_text_file(self, tmpdir: Path):
        file_path = Path(tmpdir) / "test_file.txt"
        expected = [1, 2, 3, 4, 5, 6]
        with open(file_path, "w") as f:
            f.write(",".join(map(str, expected)))
        actual = load_integers(file_path)
        assert actual == expected

    def test_should_load_integers_from_json_file(self, tmpdir: Path):
        file_path = Path(tmpdir) / "test_file.json"
        expected = [1, 2, 3, 4, 5, 6]
        with open(file_path, "w") as f:
            json.dump(expected, f)
        actual = load_integers(file_path)
        assert actual == expected

    def test_should_raise_valueerror_if_file_suffix_is_not_supported(
        self, tmpdir: Path
    ):
        file_path = Path(tmpdir) / "test_file.data"
        with open(file_path, "w") as f:
            f.write("file content")
        match_message = "File suffix .data is not supported"
        with pytest.raises(ValueError, match=match_message):
            load_integers(file_path)


class TestPathClass:
    """Verifying some assumptions."""

    def test_path_suffix_includes_leading_dot(self):
        file_path = Path("./some_file.suffix")
        assert file_path.suffix == ".suffix"

    def test_path_suffix_is_emtpy_if_no_suffix_given(self):
        file_path = Path("./some_file")
        assert file_path.suffix == ""


if __name__ == "__main__":
    txt_finder = IdFinder("testfile", ".", "txt")
    print(f"Id 5 exists in {txt_finder.file_path}: {txt_finder.contains(5)}")
    print(f"Id 15 exists in {txt_finder.file_path}: {txt_finder.contains(15)}")

    json_finder = IdFinder("testfile", ".", "json")
    print(f"Id 3 exists in {json_finder.file_path}: {json_finder.contains(3)}")
    print(f"Id 20 exists in {json_finder.file_path}: {json_finder.contains(20)}")
