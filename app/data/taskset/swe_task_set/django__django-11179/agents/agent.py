import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('19fc6376ce67d01ca37a91ef2f55ef769f50513a')
        print(f"Checked out 19fc6376ce67d01ca37a91ef2f55ef769f50513a")
    except Exception as e:
        print(f"Failed to check out 19fc6376ce67d01ca37a91ef2f55ef769f50513a: {e}")

if __name__ == "__main__":
    main()
