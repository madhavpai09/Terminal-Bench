import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('e3d1f9ac39e4bf0f31430e779acc50fb05fe1b64')
        print(f"Checked out e3d1f9ac39e4bf0f31430e779acc50fb05fe1b64")
    except Exception as e:
        print(f"Failed to check out e3d1f9ac39e4bf0f31430e779acc50fb05fe1b64: {e}")

if __name__ == "__main__":
    main()
