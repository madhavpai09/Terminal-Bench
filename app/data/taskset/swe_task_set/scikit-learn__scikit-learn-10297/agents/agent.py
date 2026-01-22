import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('b90661d6a46aa3619d3eec94d5281f5888add501')
        print(f"Checked out b90661d6a46aa3619d3eec94d5281f5888add501")
    except Exception as e:
        print(f"Failed to check out b90661d6a46aa3619d3eec94d5281f5888add501: {e}")

if __name__ == "__main__":
    main()
