import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('e886ce4e1444c61b865e7839c9cff5464ee20ace')
        print(f"Checked out e886ce4e1444c61b865e7839c9cff5464ee20ace")
    except Exception as e:
        print(f"Failed to check out e886ce4e1444c61b865e7839c9cff5464ee20ace: {e}")

if __name__ == "__main__":
    main()
