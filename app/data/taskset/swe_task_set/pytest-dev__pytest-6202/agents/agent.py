import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pytest-dev/pytest"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('3a668ea6ff24b0c8f00498c3144c63bac561d925')
        print(f"Checked out 3a668ea6ff24b0c8f00498c3144c63bac561d925")
    except Exception as e:
        print(f"Failed to check out 3a668ea6ff24b0c8f00498c3144c63bac561d925: {e}")

if __name__ == "__main__":
    main()
