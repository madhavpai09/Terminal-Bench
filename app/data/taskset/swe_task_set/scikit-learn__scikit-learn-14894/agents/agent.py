import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('fdbaa58acbead5a254f2e6d597dc1ab3b947f4c6')
        print(f"Checked out fdbaa58acbead5a254f2e6d597dc1ab3b947f4c6")
    except Exception as e:
        print(f"Failed to check out fdbaa58acbead5a254f2e6d597dc1ab3b947f4c6: {e}")

if __name__ == "__main__":
    main()
