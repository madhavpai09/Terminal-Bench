import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('dab48b7482295956973879d15bfd4d3bb0718772')
        print(f"Checked out dab48b7482295956973879d15bfd4d3bb0718772")
    except Exception as e:
        print(f"Failed to check out dab48b7482295956973879d15bfd4d3bb0718772: {e}")

if __name__ == "__main__":
    main()
