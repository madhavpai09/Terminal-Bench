import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('7f33c1e22dbc34a7afae7967783725b10f1f13b1')
        print(f"Checked out 7f33c1e22dbc34a7afae7967783725b10f1f13b1")
    except Exception as e:
        print(f"Failed to check out 7f33c1e22dbc34a7afae7967783725b10f1f13b1: {e}")

if __name__ == "__main__":
    main()
