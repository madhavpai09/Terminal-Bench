import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('5e04e84d67da8163f365e9f5fcd169e2630e2873')
        print(f"Checked out 5e04e84d67da8163f365e9f5fcd169e2630e2873")
    except Exception as e:
        print(f"Failed to check out 5e04e84d67da8163f365e9f5fcd169e2630e2873: {e}")

if __name__ == "__main__":
    main()
