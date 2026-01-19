from pathlib import Path
import sys
import pdb


shared_namespace = {
    "data_input": 100,
}

def test_solution():
    solution_string = Path("agent.py").read_text()
    verify_string = Path("solution.py").read_text()
    exec(solution_string, shared_namespace)
    exec(verify_string, shared_namespace)

if __name__ == "__main__":
    test_solution()

