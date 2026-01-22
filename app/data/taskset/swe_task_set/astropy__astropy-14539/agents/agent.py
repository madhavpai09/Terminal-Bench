import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/astropy/astropy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('c0a24c1dc957a3b565294213f435fefb2ec99714')
        print(f"Checked out c0a24c1dc957a3b565294213f435fefb2ec99714")
    except Exception as e:
        print(f"Failed to check out c0a24c1dc957a3b565294213f435fefb2ec99714: {e}")

if __name__ == "__main__":
    main()
