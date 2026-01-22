import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/astropy/astropy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('a3f4ae6cd24d5ecdf49f213d77b3513dd509a06c')
        print(f"Checked out a3f4ae6cd24d5ecdf49f213d77b3513dd509a06c")
    except Exception as e:
        print(f"Failed to check out a3f4ae6cd24d5ecdf49f213d77b3513dd509a06c: {e}")

if __name__ == "__main__":
    main()
