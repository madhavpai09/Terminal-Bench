import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('68aa4fb29e7dfe521749e1e14f750d7afabb3481')
        print(f"Checked out 68aa4fb29e7dfe521749e1e14f750d7afabb3481")
    except Exception as e:
        print(f"Failed to check out 68aa4fb29e7dfe521749e1e14f750d7afabb3481: {e}")

if __name__ == "__main__":
    main()
