import pytest
import subprocess

def pytest_addoption(parser):
    parser.addoption("--input", action="store")
    parser.addoption("--output", action="store")

@pytest.fixture()
def input_file_path(request):
    return request.config.getoption("--input")

@pytest.fixture()
def output_file_path(request):
    return request.config.getoption("--output")


class Helper:
    @staticmethod
    def get_simulation_output(input_file_path: str) -> str:
        cmd = f"cat {input_file_path} | python main.py"
    
        try:
            simulation_process = subprocess.run(cmd, shell=True, capture_output=True,
                                                text=True, timeout=10) # Adjust timeout as needed
            return simulation_process.stdout
        except subprocess.TimeoutExpired:
            return "Simulation process timed out"
    
    @staticmethod
    def compare_file_contents(content1, content2):
        lines1 = content1.splitlines()
        lines2 = content2.splitlines()
        
        for line_number, (line1, line2) in enumerate(zip(lines1, lines2), 1):
            assert line1 == line2, f"Files differ at line {line_number}"


@pytest.fixture()
def helpers():
    return Helper