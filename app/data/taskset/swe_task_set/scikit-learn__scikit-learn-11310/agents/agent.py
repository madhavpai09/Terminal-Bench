import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('553b5fb8f84ba05c8397f26dd079deece2b05029')
        print(f"Checked out 553b5fb8f84ba05c8397f26dd079deece2b05029")
    except Exception as e:
        print(f"Failed to check out 553b5fb8f84ba05c8397f26dd079deece2b05029: {e}")

if __name__ == "__main__":
    main()
