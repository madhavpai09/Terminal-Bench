import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('82ef497a8c88f0f6e50d84520e7276bfbf65025d')
        print(f"Checked out 82ef497a8c88f0f6e50d84520e7276bfbf65025d")
    except Exception as e:
        print(f"Failed to check out 82ef497a8c88f0f6e50d84520e7276bfbf65025d: {e}")

if __name__ == "__main__":
    main()
