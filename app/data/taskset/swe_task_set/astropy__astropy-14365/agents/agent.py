import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/astropy/astropy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('7269fa3e33e8d02485a647da91a5a2a60a06af61')
        print(f"Checked out 7269fa3e33e8d02485a647da91a5a2a60a06af61")
    except Exception as e:
        print(f"Failed to check out 7269fa3e33e8d02485a647da91a5a2a60a06af61: {e}")

if __name__ == "__main__":
    main()
