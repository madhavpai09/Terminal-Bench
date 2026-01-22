import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('b34751b7ed02b2cfcc36037fb729d4360480a299')
        print(f"Checked out b34751b7ed02b2cfcc36037fb729d4360480a299")
    except Exception as e:
        print(f"Failed to check out b34751b7ed02b2cfcc36037fb729d4360480a299: {e}")

if __name__ == "__main__":
    main()
