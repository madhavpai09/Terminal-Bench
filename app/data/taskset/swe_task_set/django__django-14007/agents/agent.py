import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('619f26d2895d121854b1bed1b535d42b722e2eba')
        print(f"Checked out 619f26d2895d121854b1bed1b535d42b722e2eba")
    except Exception as e:
        print(f"Failed to check out 619f26d2895d121854b1bed1b535d42b722e2eba: {e}")

if __name__ == "__main__":
    main()
