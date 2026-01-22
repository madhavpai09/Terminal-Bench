import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('493d608e39d32a67173c23a7bbc47d6bfedcef61')
        print(f"Checked out 493d608e39d32a67173c23a7bbc47d6bfedcef61")
    except Exception as e:
        print(f"Failed to check out 493d608e39d32a67173c23a7bbc47d6bfedcef61: {e}")

if __name__ == "__main__":
    main()
