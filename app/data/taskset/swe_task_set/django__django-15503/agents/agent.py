import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('859a87d873ce7152af73ab851653b4e1c3ffea4c')
        print(f"Checked out 859a87d873ce7152af73ab851653b4e1c3ffea4c")
    except Exception as e:
        print(f"Failed to check out 859a87d873ce7152af73ab851653b4e1c3ffea4c: {e}")

if __name__ == "__main__":
    main()
