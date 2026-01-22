import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('6e9c5ee88fc948e05b4a7d9f82a8861ed2b0343d')
        print(f"Checked out 6e9c5ee88fc948e05b4a7d9f82a8861ed2b0343d")
    except Exception as e:
        print(f"Failed to check out 6e9c5ee88fc948e05b4a7d9f82a8861ed2b0343d: {e}")

if __name__ == "__main__":
    main()
