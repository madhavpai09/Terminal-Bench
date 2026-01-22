import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('3ea1ec84cc610f7a9f4f6b354e264565254923ff')
        print(f"Checked out 3ea1ec84cc610f7a9f4f6b354e264565254923ff")
    except Exception as e:
        print(f"Failed to check out 3ea1ec84cc610f7a9f4f6b354e264565254923ff: {e}")

if __name__ == "__main__":
    main()
