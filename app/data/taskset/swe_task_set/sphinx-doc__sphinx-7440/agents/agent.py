import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('9bb204dcabe6ba0fc422bf4a45ad0c79c680d90b')
        print(f"Checked out 9bb204dcabe6ba0fc422bf4a45ad0c79c680d90b")
    except Exception as e:
        print(f"Failed to check out 9bb204dcabe6ba0fc422bf4a45ad0c79c680d90b: {e}")

if __name__ == "__main__":
    main()
