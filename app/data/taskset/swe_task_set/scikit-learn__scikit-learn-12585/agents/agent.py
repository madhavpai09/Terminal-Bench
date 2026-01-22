import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('bfc4a566423e036fbdc9fb02765fd893e4860c85')
        print(f"Checked out bfc4a566423e036fbdc9fb02765fd893e4860c85")
    except Exception as e:
        print(f"Failed to check out bfc4a566423e036fbdc9fb02765fd893e4860c85: {e}")

if __name__ == "__main__":
    main()
