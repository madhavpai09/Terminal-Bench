import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('444b6da7cc229a58a2c476a52e45233001dc7073')
        print(f"Checked out 444b6da7cc229a58a2c476a52e45233001dc7073")
    except Exception as e:
        print(f"Failed to check out 444b6da7cc229a58a2c476a52e45233001dc7073: {e}")

if __name__ == "__main__":
    main()
