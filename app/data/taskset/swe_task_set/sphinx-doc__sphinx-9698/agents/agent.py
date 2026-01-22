import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('f050a7775dfc9000f55d023d36d925a8d02ccfa8')
        print(f"Checked out f050a7775dfc9000f55d023d36d925a8d02ccfa8")
    except Exception as e:
        print(f"Failed to check out f050a7775dfc9000f55d023d36d925a8d02ccfa8: {e}")

if __name__ == "__main__":
    main()
