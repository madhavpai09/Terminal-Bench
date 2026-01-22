import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('fa5e7e46d875d4143510944f19d79df7b1739bab')
        print(f"Checked out fa5e7e46d875d4143510944f19d79df7b1739bab")
    except Exception as e:
        print(f"Failed to check out fa5e7e46d875d4143510944f19d79df7b1739bab: {e}")

if __name__ == "__main__":
    main()
