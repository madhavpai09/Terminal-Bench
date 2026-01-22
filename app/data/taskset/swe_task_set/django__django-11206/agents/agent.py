import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('571ab44e8a8936014c22e7eebe4948d9611fd7ce')
        print(f"Checked out 571ab44e8a8936014c22e7eebe4948d9611fd7ce")
    except Exception as e:
        print(f"Failed to check out 571ab44e8a8936014c22e7eebe4948d9611fd7ce: {e}")

if __name__ == "__main__":
    main()
