import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/astropy/astropy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('d16bfe05a744909de4b27f5875fe0d4ed41ce607')
        print(f"Checked out d16bfe05a744909de4b27f5875fe0d4ed41ce607")
    except Exception as e:
        print(f"Failed to check out d16bfe05a744909de4b27f5875fe0d4ed41ce607: {e}")

if __name__ == "__main__":
    main()
