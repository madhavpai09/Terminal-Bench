from pathlib import Path

def hello_world_exists():
    hello_path = Path('/Users/jmadhavpai/Desktop/Terminal-bench/Tasks/Hello-world/results/hello.py')
    assert hello_path.exists()

