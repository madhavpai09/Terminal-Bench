import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('2c867b8f822eb7a684f0d5c4359e4426e1c9cfe0')
        print(f"Checked out 2c867b8f822eb7a684f0d5c4359e4426e1c9cfe0")
    except Exception as e:
        print(f"Failed to check out 2c867b8f822eb7a684f0d5c4359e4426e1c9cfe0: {e}")

if __name__ == "__main__":
    main()
