from pathlib import Path

from src.utils import PROJECT_ROOT, Set1, data_path


def test_data_path_returns_path_object():
    assert isinstance(data_path(), Path)


def test_data_path_no_args():
    assert data_path().name == "data"


def test_data_path_with_subdir():
    assert data_path("elastic_net").name == "elastic_net"


def test_project_root_is_absolute():
    assert PROJECT_ROOT.is_absolute()


def test_set1_keys():
    assert set(Set1.keys()) == {3, 4, 5, 6, 7, 8, 9}


def test_set1_color_count():
    for n, colors in Set1.items():
        assert len(colors) == n


def test_set1_colors_are_hex_strings():
    for colors in Set1.values():
        for color in colors:
            assert color.startswith("#"), f"{color!r} is not a hex color string"
            assert len(color) == 7, f"{color!r} is not a 6-digit hex color"
