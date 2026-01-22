import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pylint-dev/pylint"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('ca80f03a43bc39e4cc2c67dc99817b3c9f13b8a6')
        print(f"Checked out ca80f03a43bc39e4cc2c67dc99817b3c9f13b8a6")
    except Exception as e:
        print(f"Failed to check out ca80f03a43bc39e4cc2c67dc99817b3c9f13b8a6: {e}")

if __name__ == "__main__":
    main()
