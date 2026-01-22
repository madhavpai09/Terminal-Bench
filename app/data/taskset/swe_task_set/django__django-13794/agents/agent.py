import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('fe886eee36be8022f34cfe59aa61ff1c21fe01d9')
        print(f"Checked out fe886eee36be8022f34cfe59aa61ff1c21fe01d9")
    except Exception as e:
        print(f"Failed to check out fe886eee36be8022f34cfe59aa61ff1c21fe01d9: {e}")

if __name__ == "__main__":
    main()
