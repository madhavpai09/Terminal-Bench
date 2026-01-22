import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pytest-dev/pytest"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('c98bc4cd3d687fe9b392d8eecd905627191d4f06')
        print(f"Checked out c98bc4cd3d687fe9b392d8eecd905627191d4f06")
    except Exception as e:
        print(f"Failed to check out c98bc4cd3d687fe9b392d8eecd905627191d4f06: {e}")

if __name__ == "__main__":
    main()
