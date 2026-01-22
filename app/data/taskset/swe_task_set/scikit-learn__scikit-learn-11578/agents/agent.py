import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('dd69361a0d9c6ccde0d2353b00b86e0e7541a3e3')
        print(f"Checked out dd69361a0d9c6ccde0d2353b00b86e0e7541a3e3")
    except Exception as e:
        print(f"Failed to check out dd69361a0d9c6ccde0d2353b00b86e0e7541a3e3: {e}")

if __name__ == "__main__":
    main()
