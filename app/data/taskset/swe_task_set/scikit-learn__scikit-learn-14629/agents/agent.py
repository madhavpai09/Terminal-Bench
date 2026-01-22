import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('4aded39b5663d943f6a4809abacfa9cae3d7fb6a')
        print(f"Checked out 4aded39b5663d943f6a4809abacfa9cae3d7fb6a")
    except Exception as e:
        print(f"Failed to check out 4aded39b5663d943f6a4809abacfa9cae3d7fb6a: {e}")

if __name__ == "__main__":
    main()
