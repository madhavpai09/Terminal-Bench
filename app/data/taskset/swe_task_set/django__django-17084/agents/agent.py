import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('f8c43aca467b7b0c4bb0a7fa41362f90b610b8df')
        print(f"Checked out f8c43aca467b7b0c4bb0a7fa41362f90b610b8df")
    except Exception as e:
        print(f"Failed to check out f8c43aca467b7b0c4bb0a7fa41362f90b610b8df: {e}")

if __name__ == "__main__":
    main()
