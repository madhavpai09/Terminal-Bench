import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('8f0003ae902952372824c9917975fb372c026a42')
        print(f"Checked out 8f0003ae902952372824c9917975fb372c026a42")
    except Exception as e:
        print(f"Failed to check out 8f0003ae902952372824c9917975fb372c026a42: {e}")

if __name__ == "__main__":
    main()
