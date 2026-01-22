import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('3dd06a46750d174f821df5377996f493f1af4ebb')
        print(f"Checked out 3dd06a46750d174f821df5377996f493f1af4ebb")
    except Exception as e:
        print(f"Failed to check out 3dd06a46750d174f821df5377996f493f1af4ebb: {e}")

if __name__ == "__main__":
    main()
