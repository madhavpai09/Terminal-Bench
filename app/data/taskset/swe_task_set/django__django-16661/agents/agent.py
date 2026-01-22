import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('d687febce5868545f99974d2499a91f81a32fef5')
        print(f"Checked out d687febce5868545f99974d2499a91f81a32fef5")
    except Exception as e:
        print(f"Failed to check out d687febce5868545f99974d2499a91f81a32fef5: {e}")

if __name__ == "__main__":
    main()
