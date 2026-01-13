from pathlib import Path

def test_hello_world_exists():
    hello_path = Path("/desktop/hello.py") 
    assert hello_path.exists(), f"File {hello_path} does not exist."

def test_hello_world_content():
    hello_path = Path("/desktop/hello.py")
    with open(hello_path, "r") as file:
        content = file.read()
    assert 'print("Hello, world!")' in content, "Hello World print statement not found in hello.py."