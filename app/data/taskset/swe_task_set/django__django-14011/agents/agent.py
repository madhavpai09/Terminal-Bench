import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('e4430f22c8e3d29ce5d9d0263fba57121938d06d')
        print(f"Checked out e4430f22c8e3d29ce5d9d0263fba57121938d06d")
    except Exception as e:
        print(f"Failed to check out e4430f22c8e3d29ce5d9d0263fba57121938d06d: {e}")

if __name__ == "__main__":
    main()
