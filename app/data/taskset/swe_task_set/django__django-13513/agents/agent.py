import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('6599608c4d0befdcb820ddccce55f183f247ae4f')
        print(f"Checked out 6599608c4d0befdcb820ddccce55f183f247ae4f")
    except Exception as e:
        print(f"Failed to check out 6599608c4d0befdcb820ddccce55f183f247ae4f: {e}")

if __name__ == "__main__":
    main()
