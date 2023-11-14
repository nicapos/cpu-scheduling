import pytest
from conftest import Helper
from utils import get_test_files

test_files = get_test_files("sjf")

@pytest.mark.parametrize("input_file_path,output_file_path", test_files)
def test_simulation(input_file_path, output_file_path, helpers: Helper):
    with open(output_file_path, "r") as f:
        expected_output = f.read()

    actual_output = helpers.get_simulation_output(input_file_path)

    helpers.compare_file_contents(expected_output, actual_output)