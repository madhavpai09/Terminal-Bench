import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pytest-dev/pytest"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('6e7dc8bac831cd8cf7a53b08efa366bd84f0c0fe')
        print(f"Checked out 6e7dc8bac831cd8cf7a53b08efa366bd84f0c0fe")
    except Exception as e:
        print(f"Failed to check out 6e7dc8bac831cd8cf7a53b08efa366bd84f0c0fe: {e}")

if __name__ == "__main__":
    main()
