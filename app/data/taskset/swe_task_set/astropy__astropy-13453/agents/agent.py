import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/astropy/astropy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('19cc80471739bcb67b7e8099246b391c355023ee')
        print(f"Checked out 19cc80471739bcb67b7e8099246b391c355023ee")
    except Exception as e:
        print(f"Failed to check out 19cc80471739bcb67b7e8099246b391c355023ee: {e}")

if __name__ == "__main__":
    main()
