import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pallets/flask"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('7ee9ceb71e868944a46e1ff00b506772a53a4f1d')
        print(f"Checked out 7ee9ceb71e868944a46e1ff00b506772a53a4f1d")
    except Exception as e:
        print(f"Failed to check out 7ee9ceb71e868944a46e1ff00b506772a53a4f1d: {e}")

if __name__ == "__main__":
    main()
