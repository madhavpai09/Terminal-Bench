import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('876fa81e0a038cda466925b85ccf6c5452e0f685')
        print(f"Checked out 876fa81e0a038cda466925b85ccf6c5452e0f685")
    except Exception as e:
        print(f"Failed to check out 876fa81e0a038cda466925b85ccf6c5452e0f685: {e}")

if __name__ == "__main__":
    main()
