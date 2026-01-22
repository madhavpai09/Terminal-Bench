import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('67f9d076cfc1858b94f9ed6d1a5ce2327dcc8d0d')
        print(f"Checked out 67f9d076cfc1858b94f9ed6d1a5ce2327dcc8d0d")
    except Exception as e:
        print(f"Failed to check out 67f9d076cfc1858b94f9ed6d1a5ce2327dcc8d0d: {e}")

if __name__ == "__main__":
    main()
