import pytest
from Sort.shell_sort import shell_sort


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ([89, 65, 23, 55, 15, 62, 23, 1, 34, 10], 
         [1, 10, 15, 23, 23, 34, 55, 62, 65, 89])
    ], 
)
def test_shell_sort(input_data, expected):
    assert shell_sort(input_data) == expected

    