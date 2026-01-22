import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('d49a6f13af2f22228d430ac64ac2b518937800d0')
        print(f"Checked out d49a6f13af2f22228d430ac64ac2b518937800d0")
    except Exception as e:
        print(f"Failed to check out d49a6f13af2f22228d430ac64ac2b518937800d0: {e}")

if __name__ == "__main__":
    main()
