from pathlib import Path

def hello_world_content():
    hello_path = Path('/Users/jmadhavpai/Desktop/Terminal-bench/Tasks/Hello-world/results/hello.py')
    content = hello_path.read_text()
    assert content == "print('Hellly, world!')\n"
