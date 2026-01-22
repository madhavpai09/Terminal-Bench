import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('b428cd2404675475a5c3dc2a2b0790ba57676202')
        print(f"Checked out b428cd2404675475a5c3dc2a2b0790ba57676202")
    except Exception as e:
        print(f"Failed to check out b428cd2404675475a5c3dc2a2b0790ba57676202: {e}")

if __name__ == "__main__":
    main()
