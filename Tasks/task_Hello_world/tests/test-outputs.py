from pathlib import Path

def hello_world_exists():
    hello_path = Path('/Users/jmadhavpai/Desktop/Terminal-bench/Tasks/Hello-world/results/hello.py')
    assert hello_path.exists()

def hello_world_content():
    hello_path = Path('/Users/jmadhavpai/Desktop/Terminal-bench/Tasks/Hello-world/results/hello.py')
    content = hello_path.read_text()
    assert content == "print('Hello, world!')\n"

def test_hello_world():
    hello_path = Path('/Users/jmadhavpai/Desktop/Terminal-bench/Tasks/Hello-world/results/result.txt')
    content = hello_path.read_text()
    assert content == "Hello, world!"

print("Succesful")