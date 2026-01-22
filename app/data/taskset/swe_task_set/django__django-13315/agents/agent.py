import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('36bc47069ce071e80c8129500de3b8664d2058a7')
        print(f"Checked out 36bc47069ce071e80c8129500de3b8664d2058a7")
    except Exception as e:
        print(f"Failed to check out 36bc47069ce071e80c8129500de3b8664d2058a7: {e}")

if __name__ == "__main__":
    main()
