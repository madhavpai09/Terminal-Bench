import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pylint-dev/pylint"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('1d1619ef913b99b06647d2030bddff4800abdf63')
        print(f"Checked out 1d1619ef913b99b06647d2030bddff4800abdf63")
    except Exception as e:
        print(f"Failed to check out 1d1619ef913b99b06647d2030bddff4800abdf63: {e}")

if __name__ == "__main__":
    main()
