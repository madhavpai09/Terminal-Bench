import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/psf/requests"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('39d0fdd9096f7dceccbc8f82e1eda7dd64717a8e')
        print(f"Checked out 39d0fdd9096f7dceccbc8f82e1eda7dd64717a8e")
    except Exception as e:
        print(f"Failed to check out 39d0fdd9096f7dceccbc8f82e1eda7dd64717a8e: {e}")

if __name__ == "__main__":
    main()
