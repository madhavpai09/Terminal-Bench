import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pydata/xarray"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('8cc34cb412ba89ebca12fc84f76a9e452628f1bc')
        print(f"Checked out 8cc34cb412ba89ebca12fc84f76a9e452628f1bc")
    except Exception as e:
        print(f"Failed to check out 8cc34cb412ba89ebca12fc84f76a9e452628f1bc: {e}")

if __name__ == "__main__":
    main()
