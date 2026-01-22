import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('e02f67ef2d03d48128e7a118bf75f0418e24e8ac')
        print(f"Checked out e02f67ef2d03d48128e7a118bf75f0418e24e8ac")
    except Exception as e:
        print(f"Failed to check out e02f67ef2d03d48128e7a118bf75f0418e24e8ac: {e}")

if __name__ == "__main__":
    main()
