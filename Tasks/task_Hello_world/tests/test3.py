from pathlib import Path

def test_hello_world():
    hello_path = Path('/Users/jmadhavpai/Desktop/Terminal-bench/Tasks/Hello-world/results/result.txt')
    content = hello_path.read_text()
    assert content == "Hellly, world!"