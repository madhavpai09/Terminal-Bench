import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('f30284ef926ebaf04b176f21b421e2dffc679792')
        print(f"Checked out f30284ef926ebaf04b176f21b421e2dffc679792")
    except Exception as e:
        print(f"Failed to check out f30284ef926ebaf04b176f21b421e2dffc679792: {e}")

if __name__ == "__main__":
    main()
