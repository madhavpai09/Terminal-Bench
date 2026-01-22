import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pytest-dev/pytest"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('a7e38c5c61928033a2dc1915cbee8caa8544a4d0')
        print(f"Checked out a7e38c5c61928033a2dc1915cbee8caa8544a4d0")
    except Exception as e:
        print(f"Failed to check out a7e38c5c61928033a2dc1915cbee8caa8544a4d0: {e}")

if __name__ == "__main__":
    main()
