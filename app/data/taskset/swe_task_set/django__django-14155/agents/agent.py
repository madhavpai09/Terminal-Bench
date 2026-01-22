import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('2f13c476abe4ba787b6cb71131818341911f43cc')
        print(f"Checked out 2f13c476abe4ba787b6cb71131818341911f43cc")
    except Exception as e:
        print(f"Failed to check out 2f13c476abe4ba787b6cb71131818341911f43cc: {e}")

if __name__ == "__main__":
    main()
