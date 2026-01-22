import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pylint-dev/pylint"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('1e55ae64624d28c5fe8b63ad7979880ee2e6ef3f')
        print(f"Checked out 1e55ae64624d28c5fe8b63ad7979880ee2e6ef3f")
    except Exception as e:
        print(f"Failed to check out 1e55ae64624d28c5fe8b63ad7979880ee2e6ef3f: {e}")

if __name__ == "__main__":
    main()
