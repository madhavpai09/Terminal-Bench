import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('3aefc834dce72e850bff48689bea3c7dff5f3fad')
        print(f"Checked out 3aefc834dce72e850bff48689bea3c7dff5f3fad")
    except Exception as e:
        print(f"Failed to check out 3aefc834dce72e850bff48689bea3c7dff5f3fad: {e}")

if __name__ == "__main__":
    main()
