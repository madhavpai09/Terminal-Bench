import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/psf/requests"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('0192aac24123735b3eaf9b08df46429bb770c283')
        print(f"Checked out 0192aac24123735b3eaf9b08df46429bb770c283")
    except Exception as e:
        print(f"Failed to check out 0192aac24123735b3eaf9b08df46429bb770c283: {e}")

if __name__ == "__main__":
    main()
