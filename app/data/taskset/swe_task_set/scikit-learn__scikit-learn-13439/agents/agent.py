import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('a62775e99f2a5ea3d51db7160fad783f6cd8a4c5')
        print(f"Checked out a62775e99f2a5ea3d51db7160fad783f6cd8a4c5")
    except Exception as e:
        print(f"Failed to check out a62775e99f2a5ea3d51db7160fad783f6cd8a4c5: {e}")

if __name__ == "__main__":
    main()
