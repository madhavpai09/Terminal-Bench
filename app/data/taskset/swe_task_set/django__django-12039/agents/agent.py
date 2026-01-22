import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('58c1acb1d6054dfec29d0f30b1033bae6ef62aec')
        print(f"Checked out 58c1acb1d6054dfec29d0f30b1033bae6ef62aec")
    except Exception as e:
        print(f"Failed to check out 58c1acb1d6054dfec29d0f30b1033bae6ef62aec: {e}")

if __name__ == "__main__":
    main()
