import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('97fc1154992f64cfb2f86321155a7404efeb2d8a')
        print(f"Checked out 97fc1154992f64cfb2f86321155a7404efeb2d8a")
    except Exception as e:
        print(f"Failed to check out 97fc1154992f64cfb2f86321155a7404efeb2d8a: {e}")

if __name__ == "__main__":
    main()
