import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('232dbe41c5250eb7d559d40438c4743483e95f15')
        print(f"Checked out 232dbe41c5250eb7d559d40438c4743483e95f15")
    except Exception as e:
        print(f"Failed to check out 232dbe41c5250eb7d559d40438c4743483e95f15: {e}")

if __name__ == "__main__":
    main()
