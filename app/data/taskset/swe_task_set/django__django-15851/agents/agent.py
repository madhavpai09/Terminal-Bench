import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('b4817d20b9e55df30be0b1b2ca8c8bb6d61aab07')
        print(f"Checked out b4817d20b9e55df30be0b1b2ca8c8bb6d61aab07")
    except Exception as e:
        print(f"Failed to check out b4817d20b9e55df30be0b1b2ca8c8bb6d61aab07: {e}")

if __name__ == "__main__":
    main()
