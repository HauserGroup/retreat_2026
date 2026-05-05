from src.utils import Set1, data_path


def test_data_path_no_args():
    assert data_path().name == "data"


def test_data_path_with_subdir():
    assert data_path("elastic_net").name == "elastic_net"


def test_set1_keys():
    assert set(Set1.keys()) == {3, 4, 5, 6, 7, 8, 9}


def test_set1_color_count():
    for n, colors in Set1.items():
        assert len(colors) == n
