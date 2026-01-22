import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/astropy/astropy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('298ccb478e6bf092953bca67a3d29dc6c35f6752')
        print(f"Checked out 298ccb478e6bf092953bca67a3d29dc6c35f6752")
    except Exception as e:
        print(f"Failed to check out 298ccb478e6bf092953bca67a3d29dc6c35f6752: {e}")

if __name__ == "__main__":
    main()
