import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/astropy/astropy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('26d147868f8a891a6009a25cd6a8576d2e1bd747')
        print(f"Checked out 26d147868f8a891a6009a25cd6a8576d2e1bd747")
    except Exception as e:
        print(f"Failed to check out 26d147868f8a891a6009a25cd6a8576d2e1bd747: {e}")

if __name__ == "__main__":
    main()
