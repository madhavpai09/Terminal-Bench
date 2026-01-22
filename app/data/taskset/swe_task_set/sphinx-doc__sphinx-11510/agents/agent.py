import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('6cb783c0024a873722952a67ebb9f41771c8eb6d')
        print(f"Checked out 6cb783c0024a873722952a67ebb9f41771c8eb6d")
    except Exception as e:
        print(f"Failed to check out 6cb783c0024a873722952a67ebb9f41771c8eb6d: {e}")

if __name__ == "__main__":
    main()
