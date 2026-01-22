import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('97523985b39ecde369d83352d7c3baf403b60a22')
        print(f"Checked out 97523985b39ecde369d83352d7c3baf403b60a22")
    except Exception as e:
        print(f"Failed to check out 97523985b39ecde369d83352d7c3baf403b60a22: {e}")

if __name__ == "__main__":
    main()
