import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('e28671187903e6aca2428374fdd504fca3032aee')
        print(f"Checked out e28671187903e6aca2428374fdd504fca3032aee")
    except Exception as e:
        print(f"Failed to check out e28671187903e6aca2428374fdd504fca3032aee: {e}")

if __name__ == "__main__":
    main()
