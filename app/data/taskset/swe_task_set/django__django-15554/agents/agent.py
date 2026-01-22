import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('59ab3fd0e9e606d7f0f7ca26609c06ee679ece97')
        print(f"Checked out 59ab3fd0e9e606d7f0f7ca26609c06ee679ece97")
    except Exception as e:
        print(f"Failed to check out 59ab3fd0e9e606d7f0f7ca26609c06ee679ece97: {e}")

if __name__ == "__main__":
    main()
