import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('7d5329852f19c6ae78c6f6f3d3e41835377bf295')
        print(f"Checked out 7d5329852f19c6ae78c6f6f3d3e41835377bf295")
    except Exception as e:
        print(f"Failed to check out 7d5329852f19c6ae78c6f6f3d3e41835377bf295: {e}")

if __name__ == "__main__":
    main()
