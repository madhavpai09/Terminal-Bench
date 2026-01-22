import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('3d997697fdd166eff428ea9fd35734b6a8ba113e')
        print(f"Checked out 3d997697fdd166eff428ea9fd35734b6a8ba113e")
    except Exception as e:
        print(f"Failed to check out 3d997697fdd166eff428ea9fd35734b6a8ba113e: {e}")

if __name__ == "__main__":
    main()
