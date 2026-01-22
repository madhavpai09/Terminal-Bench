import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('f0adf3b9b7a19cdee05368ff0c0c2d087f011180')
        print(f"Checked out f0adf3b9b7a19cdee05368ff0c0c2d087f011180")
    except Exception as e:
        print(f"Failed to check out f0adf3b9b7a19cdee05368ff0c0c2d087f011180: {e}")

if __name__ == "__main__":
    main()
