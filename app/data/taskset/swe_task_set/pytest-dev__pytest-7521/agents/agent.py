import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pytest-dev/pytest"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('41d211c24a6781843b174379d6d6538f5c17adb9')
        print(f"Checked out 41d211c24a6781843b174379d6d6538f5c17adb9")
    except Exception as e:
        print(f"Failed to check out 41d211c24a6781843b174379d6d6538f5c17adb9: {e}")

if __name__ == "__main__":
    main()
