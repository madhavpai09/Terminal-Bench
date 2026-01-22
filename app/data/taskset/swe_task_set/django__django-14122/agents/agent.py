import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('bc04941bf811d1ea2c79fb7fc20457ed2c7e3410')
        print(f"Checked out bc04941bf811d1ea2c79fb7fc20457ed2c7e3410")
    except Exception as e:
        print(f"Failed to check out bc04941bf811d1ea2c79fb7fc20457ed2c7e3410: {e}")

if __name__ == "__main__":
    main()
