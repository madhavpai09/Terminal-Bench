import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('64619e53e9d0ed417daba287ac0d3a06943a54d5')
        print(f"Checked out 64619e53e9d0ed417daba287ac0d3a06943a54d5")
    except Exception as e:
        print(f"Failed to check out 64619e53e9d0ed417daba287ac0d3a06943a54d5: {e}")

if __name__ == "__main__":
    main()
