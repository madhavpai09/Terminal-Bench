import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('93cedc82f29076c824d476354527af1150888e4f')
        print(f"Checked out 93cedc82f29076c824d476354527af1150888e4f")
    except Exception as e:
        print(f"Failed to check out 93cedc82f29076c824d476354527af1150888e4f: {e}")

if __name__ == "__main__":
    main()
