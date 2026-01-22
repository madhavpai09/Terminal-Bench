import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('14d026cccb144c6877294ba4cd4e03ebf0842498')
        print(f"Checked out 14d026cccb144c6877294ba4cd4e03ebf0842498")
    except Exception as e:
        print(f"Failed to check out 14d026cccb144c6877294ba4cd4e03ebf0842498: {e}")

if __name__ == "__main__":
    main()
