import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('10dbc142bd17ccf7bd38eec2ac04b52ce0d1009e')
        print(f"Checked out 10dbc142bd17ccf7bd38eec2ac04b52ce0d1009e")
    except Exception as e:
        print(f"Failed to check out 10dbc142bd17ccf7bd38eec2ac04b52ce0d1009e: {e}")

if __name__ == "__main__":
    main()
