import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('2e506c5ab457cba743bb47eb5b8c8eb9dd51d23d')
        print(f"Checked out 2e506c5ab457cba743bb47eb5b8c8eb9dd51d23d")
    except Exception as e:
        print(f"Failed to check out 2e506c5ab457cba743bb47eb5b8c8eb9dd51d23d: {e}")

if __name__ == "__main__":
    main()
