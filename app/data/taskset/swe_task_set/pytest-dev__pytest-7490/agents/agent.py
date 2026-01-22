import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pytest-dev/pytest"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('7f7a36478abe7dd1fa993b115d22606aa0e35e88')
        print(f"Checked out 7f7a36478abe7dd1fa993b115d22606aa0e35e88")
    except Exception as e:
        print(f"Failed to check out 7f7a36478abe7dd1fa993b115d22606aa0e35e88: {e}")

if __name__ == "__main__":
    main()
