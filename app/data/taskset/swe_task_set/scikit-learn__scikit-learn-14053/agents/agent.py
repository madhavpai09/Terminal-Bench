import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('6ab8c86c383dd847a1be7103ad115f174fe23ffd')
        print(f"Checked out 6ab8c86c383dd847a1be7103ad115f174fe23ffd")
    except Exception as e:
        print(f"Failed to check out 6ab8c86c383dd847a1be7103ad115f174fe23ffd: {e}")

if __name__ == "__main__":
    main()
