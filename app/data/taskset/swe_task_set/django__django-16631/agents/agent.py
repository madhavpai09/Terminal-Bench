import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('9b224579875e30203d079cc2fee83b116d98eb78')
        print(f"Checked out 9b224579875e30203d079cc2fee83b116d98eb78")
    except Exception as e:
        print(f"Failed to check out 9b224579875e30203d079cc2fee83b116d98eb78: {e}")

if __name__ == "__main__":
    main()
