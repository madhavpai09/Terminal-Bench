import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('ec9af606c6cfa515f946d74da9b51574f2f9b16f')
        print(f"Checked out ec9af606c6cfa515f946d74da9b51574f2f9b16f")
    except Exception as e:
        print(f"Failed to check out ec9af606c6cfa515f946d74da9b51574f2f9b16f: {e}")

if __name__ == "__main__":
    main()
