import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('db1fc5cd3c5d36cdb5d0fe4404efd6623dd3e8fb')
        print(f"Checked out db1fc5cd3c5d36cdb5d0fe4404efd6623dd3e8fb")
    except Exception as e:
        print(f"Failed to check out db1fc5cd3c5d36cdb5d0fe4404efd6623dd3e8fb: {e}")

if __name__ == "__main__":
    main()
