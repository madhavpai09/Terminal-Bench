import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('cab2d93076d0cca7c53fac885f927dde3e2a5fec')
        print(f"Checked out cab2d93076d0cca7c53fac885f927dde3e2a5fec")
    except Exception as e:
        print(f"Failed to check out cab2d93076d0cca7c53fac885f927dde3e2a5fec: {e}")

if __name__ == "__main__":
    main()
