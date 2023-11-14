import pytest
from conftest import Helper
from utils import validate_file_path


def test_custom_case(input_file_path, output_file_path, helpers: Helper):
    validate_file_path(input_file_path)
    validate_file_path(output_file_path)

    with open(output_file_path, "r") as f:
        expected_output = f.read()

    actual_output = helpers.get_simulation_output(input_file_path)

    assert expected_output == actual_output