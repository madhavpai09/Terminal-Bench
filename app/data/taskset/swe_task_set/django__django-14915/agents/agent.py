import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('903aaa35e5ceaa33bfc9b19b7f6da65ce5a91dd4')
        print(f"Checked out 903aaa35e5ceaa33bfc9b19b7f6da65ce5a91dd4")
    except Exception as e:
        print(f"Failed to check out 903aaa35e5ceaa33bfc9b19b7f6da65ce5a91dd4: {e}")

if __name__ == "__main__":
    main()
