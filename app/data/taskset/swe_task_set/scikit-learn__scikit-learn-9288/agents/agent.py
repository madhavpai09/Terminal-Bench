import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('3eacf948e0f95ef957862568d87ce082f378e186')
        print(f"Checked out 3eacf948e0f95ef957862568d87ce082f378e186")
    except Exception as e:
        print(f"Failed to check out 3eacf948e0f95ef957862568d87ce082f378e186: {e}")

if __name__ == "__main__":
    main()
