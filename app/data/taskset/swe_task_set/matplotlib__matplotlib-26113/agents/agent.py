import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('5ca694b38d861c0e24cd8743753427dda839b90b')
        print(f"Checked out 5ca694b38d861c0e24cd8743753427dda839b90b")
    except Exception as e:
        print(f"Failed to check out 5ca694b38d861c0e24cd8743753427dda839b90b: {e}")

if __name__ == "__main__":
    main()
