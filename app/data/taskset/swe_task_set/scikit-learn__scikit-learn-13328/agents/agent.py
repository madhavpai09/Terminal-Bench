import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('37b0e66c871e8fb032a9c7086b2a1d5419838154')
        print(f"Checked out 37b0e66c871e8fb032a9c7086b2a1d5419838154")
    except Exception as e:
        print(f"Failed to check out 37b0e66c871e8fb032a9c7086b2a1d5419838154: {e}")

if __name__ == "__main__":
    main()
