import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('156a2138db20abc89933121e4ff2ee2ce56a173a')
        print(f"Checked out 156a2138db20abc89933121e4ff2ee2ce56a173a")
    except Exception as e:
        print(f"Failed to check out 156a2138db20abc89933121e4ff2ee2ce56a173a: {e}")

if __name__ == "__main__":
    main()
