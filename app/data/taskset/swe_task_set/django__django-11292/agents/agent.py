import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('eb16c7260e573ec513d84cb586d96bdf508f3173')
        print(f"Checked out eb16c7260e573ec513d84cb586d96bdf508f3173")
    except Exception as e:
        print(f"Failed to check out eb16c7260e573ec513d84cb586d96bdf508f3173: {e}")

if __name__ == "__main__":
    main()
