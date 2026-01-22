import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('7fa1a93c6c8109010a6ff3f604fda83b604e0e97')
        print(f"Checked out 7fa1a93c6c8109010a6ff3f604fda83b604e0e97")
    except Exception as e:
        print(f"Failed to check out 7fa1a93c6c8109010a6ff3f604fda83b604e0e97: {e}")

if __name__ == "__main__":
    main()
