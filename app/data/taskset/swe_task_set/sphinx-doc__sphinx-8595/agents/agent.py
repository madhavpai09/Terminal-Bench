import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('b19bce971e82f2497d67fdacdeca8db08ae0ba56')
        print(f"Checked out b19bce971e82f2497d67fdacdeca8db08ae0ba56")
    except Exception as e:
        print(f"Failed to check out b19bce971e82f2497d67fdacdeca8db08ae0ba56: {e}")

if __name__ == "__main__":
    main()
