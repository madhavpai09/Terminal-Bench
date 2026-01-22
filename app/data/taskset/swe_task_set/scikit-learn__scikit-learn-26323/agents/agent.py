import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('586f4318ffcdfbd9a1093f35ad43e81983740b66')
        print(f"Checked out 586f4318ffcdfbd9a1093f35ad43e81983740b66")
    except Exception as e:
        print(f"Failed to check out 586f4318ffcdfbd9a1093f35ad43e81983740b66: {e}")

if __name__ == "__main__":
    main()
