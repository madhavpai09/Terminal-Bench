import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('9d22ab09d52d279b125d8770967569de070913b2')
        print(f"Checked out 9d22ab09d52d279b125d8770967569de070913b2")
    except Exception as e:
        print(f"Failed to check out 9d22ab09d52d279b125d8770967569de070913b2: {e}")

if __name__ == "__main__":
    main()
