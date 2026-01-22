import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('66ba515e671638971bd11a34cff12c107a437e0b')
        print(f"Checked out 66ba515e671638971bd11a34cff12c107a437e0b")
    except Exception as e:
        print(f"Failed to check out 66ba515e671638971bd11a34cff12c107a437e0b: {e}")

if __name__ == "__main__":
    main()
