import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('999891bd80b3d02dd916731a7a239e1036174885')
        print(f"Checked out 999891bd80b3d02dd916731a7a239e1036174885")
    except Exception as e:
        print(f"Failed to check out 999891bd80b3d02dd916731a7a239e1036174885: {e}")

if __name__ == "__main__":
    main()
