import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('55bcbd8d172b689811fae17cde2f09218dd74e9c')
        print(f"Checked out 55bcbd8d172b689811fae17cde2f09218dd74e9c")
    except Exception as e:
        print(f"Failed to check out 55bcbd8d172b689811fae17cde2f09218dd74e9c: {e}")

if __name__ == "__main__":
    main()
