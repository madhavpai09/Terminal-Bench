import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('76e37513e22f4d9a01c7f15eee36fe44388e6670')
        print(f"Checked out 76e37513e22f4d9a01c7f15eee36fe44388e6670")
    except Exception as e:
        print(f"Failed to check out 76e37513e22f4d9a01c7f15eee36fe44388e6670: {e}")

if __name__ == "__main__":
    main()
