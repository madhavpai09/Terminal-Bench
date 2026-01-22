import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pydata/xarray"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('1757dffac2fa493d7b9a074b84cf8c830a706688')
        print(f"Checked out 1757dffac2fa493d7b9a074b84cf8c830a706688")
    except Exception as e:
        print(f"Failed to check out 1757dffac2fa493d7b9a074b84cf8c830a706688: {e}")

if __name__ == "__main__":
    main()
