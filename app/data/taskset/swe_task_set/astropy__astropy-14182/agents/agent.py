import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/astropy/astropy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('a5917978be39d13cd90b517e1de4e7a539ffaa48')
        print(f"Checked out a5917978be39d13cd90b517e1de4e7a539ffaa48")
    except Exception as e:
        print(f"Failed to check out a5917978be39d13cd90b517e1de4e7a539ffaa48: {e}")

if __name__ == "__main__":
    main()
