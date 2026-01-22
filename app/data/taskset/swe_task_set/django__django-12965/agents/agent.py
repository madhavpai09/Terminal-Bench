import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('437196da9a386bd4cc62b0ce3f2de4aba468613d')
        print(f"Checked out 437196da9a386bd4cc62b0ce3f2de4aba468613d")
    except Exception as e:
        print(f"Failed to check out 437196da9a386bd4cc62b0ce3f2de4aba468613d: {e}")

if __name__ == "__main__":
    main()
