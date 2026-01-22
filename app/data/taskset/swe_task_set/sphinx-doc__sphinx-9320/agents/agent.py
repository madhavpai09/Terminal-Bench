import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('e05cef574b8f23ab1b57f57e7da6dee509a4e230')
        print(f"Checked out e05cef574b8f23ab1b57f57e7da6dee509a4e230")
    except Exception as e:
        print(f"Failed to check out e05cef574b8f23ab1b57f57e7da6dee509a4e230: {e}")

if __name__ == "__main__":
    main()
