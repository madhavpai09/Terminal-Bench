import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('179ee13eb37348cd87169a198aec18fedccc8668')
        print(f"Checked out 179ee13eb37348cd87169a198aec18fedccc8668")
    except Exception as e:
        print(f"Failed to check out 179ee13eb37348cd87169a198aec18fedccc8668: {e}")

if __name__ == "__main__":
    main()
