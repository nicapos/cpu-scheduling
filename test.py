import subprocess
import argparse

from test.utils import ALGORITHMS, color_string, validate_file_path, get_test_files

def test_output_matches_expected(input_file_path: str, expected_output_file_path: str) -> bool:
    """Returns True if the output of the simulation matches the expected output, False otherwise"""

    cmd = f"cat {input_file_path} | python main.py"
    simulation_process = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    actual_output = simulation_process.stdout

    with open(expected_output_file_path, "r") as f:
        expected_output = f.read()

    return actual_output == expected_output


def run_test_algorithm(algorithm_name: str):    
    input_files, output_files = get_test_files(algorithm_name)

    num_tests = len(input_files)
    print(f"Running {num_tests} tests for {algorithm_name}...\n")

    for i in range(num_tests):
        is_match = test_output_matches_expected(input_files[i], output_files[i])
        result = color_string('PASSED', 'green') if is_match else color_string('FAILED', 'red')

        print(input_files[i], result)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, help='Path to the input file')
    parser.add_argument('-o', '--output', type=str, help='Path to the expected output file')
    parser.add_argument('--algo', type=str, help='Name of the algorithm to test')

    args = parser.parse_args()

    if args.input is not None and args.output is not None:
        validate_file_path(args.input)
        validate_file_path(args.output)

        is_match = test_output_matches_expected(args.input, args.output)
        result = color_string('PASSED', 'green') if is_match else color_string('FAILED', 'red')

        print(args.input, result)

    elif args.algo is not None:
        algorithm = args.algo.upper()
        if algorithm not in ALGORITHMS:
            raise Exception(f"Invalid algorithm name (passed {algorithm})")
        
        run_test_algorithm(algorithm)

    else:
        # Test everything if no algorithm is specified
        for algo_name in ALGORITHMS:
            run_test_algorithm(algo_name)
            print()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"ERROR: {e}")