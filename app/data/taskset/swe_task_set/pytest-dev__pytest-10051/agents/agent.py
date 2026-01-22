import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pytest-dev/pytest"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('aa55975c7d3f6c9f6d7f68accc41bb7cadf0eb9a')
        print(f"Checked out aa55975c7d3f6c9f6d7f68accc41bb7cadf0eb9a")
    except Exception as e:
        print(f"Failed to check out aa55975c7d3f6c9f6d7f68accc41bb7cadf0eb9a: {e}")

if __name__ == "__main__":
    main()
