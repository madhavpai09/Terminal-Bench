import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pydata/xarray"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('e05fddea852d08fc0845f954b79deb9e9f9ff883')
        print(f"Checked out e05fddea852d08fc0845f954b79deb9e9f9ff883")
    except Exception as e:
        print(f"Failed to check out e05fddea852d08fc0845f954b79deb9e9f9ff883: {e}")

if __name__ == "__main__":
    main()
