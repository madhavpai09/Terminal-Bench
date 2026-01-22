import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('14c96b510ebeba40f573e512299b1976f35b620e')
        print(f"Checked out 14c96b510ebeba40f573e512299b1976f35b620e")
    except Exception as e:
        print(f"Failed to check out 14c96b510ebeba40f573e512299b1976f35b620e: {e}")

if __name__ == "__main__":
    main()
