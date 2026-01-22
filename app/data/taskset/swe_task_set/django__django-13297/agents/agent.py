import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('8954f255bbf5f4ee997fd6de62cb50fc9b5dd697')
        print(f"Checked out 8954f255bbf5f4ee997fd6de62cb50fc9b5dd697")
    except Exception as e:
        print(f"Failed to check out 8954f255bbf5f4ee997fd6de62cb50fc9b5dd697: {e}")

if __name__ == "__main__":
    main()
