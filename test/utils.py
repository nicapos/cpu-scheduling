from imghdr import tests
import os

ALGORITHMS = ["FCFS", "SJF", "SRTF", "RR"]

def color_string(string: str, color: str) -> str:
    color_code = {
        'red': '\033[91m',
        'green': '\033[92m',
        'reset': '\033[0m'
    }

    return color_code[color] + string + color_code['reset']


def validate_file_path(file_path: str):
    if not (os.path.isfile(file_path) or os.path.exists(file_path)):
        raise Exception(f"Invalid input file path (passed '{file_path}')")
    

def get_test_files(algorithm_name: str) -> tuple[list[str], list[str]]:
    """Returns a tuple of lists containing the input and output file paths for the given algorithm"""
    tests_directory = os.path.join('test', algorithm_name.upper())

    # Get all input files
    input_files = [f for f in os.listdir(tests_directory) if f.startswith("input")]
    input_files.sort()

    # For each input file, check if there is a corresponding output file
    output_files = []
    for input_file in input_files:
        output_file = input_file.replace("input", "output")

        if output_file not in os.listdir(tests_directory):
            raise Exception(f"Missing output file for {input_file}")

        output_files.append(output_file)

    input_file_paths = [os.path.join(tests_directory, f) for f in input_files]
    output_file_paths = [os.path.join(tests_directory, f) for f in output_files]

    # Returns paths to input files and output files as parallel lists
    return input_file_paths, output_file_paths