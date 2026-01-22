import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('f9fe062de5fc0896d6bbbf3f260b5c44473b3c77')
        print(f"Checked out f9fe062de5fc0896d6bbbf3f260b5c44473b3c77")
    except Exception as e:
        print(f"Failed to check out f9fe062de5fc0896d6bbbf3f260b5c44473b3c77: {e}")

if __name__ == "__main__":
    main()
