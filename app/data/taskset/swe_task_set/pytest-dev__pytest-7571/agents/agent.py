import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pytest-dev/pytest"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('422685d0bdc110547535036c1ff398b5e1c44145')
        print(f"Checked out 422685d0bdc110547535036c1ff398b5e1c44145")
    except Exception as e:
        print(f"Failed to check out 422685d0bdc110547535036c1ff398b5e1c44145: {e}")

if __name__ == "__main__":
    main()
