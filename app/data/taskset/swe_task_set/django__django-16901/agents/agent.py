import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('ee36e101e8f8c0acde4bb148b738ab7034e902a0')
        print(f"Checked out ee36e101e8f8c0acde4bb148b738ab7034e902a0")
    except Exception as e:
        print(f"Failed to check out ee36e101e8f8c0acde4bb148b738ab7034e902a0: {e}")

if __name__ == "__main__":
    main()
