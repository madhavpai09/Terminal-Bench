import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('6991880109e35c879b71b7d9d9c154baeec12b89')
        print(f"Checked out 6991880109e35c879b71b7d9d9c154baeec12b89")
    except Exception as e:
        print(f"Failed to check out 6991880109e35c879b71b7d9d9c154baeec12b89: {e}")

if __name__ == "__main__":
    main()
