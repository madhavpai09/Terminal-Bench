import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('55b68de643b5c2d5f0a8ea7587ab3b2966021ccc')
        print(f"Checked out 55b68de643b5c2d5f0a8ea7587ab3b2966021ccc")
    except Exception as e:
        print(f"Failed to check out 55b68de643b5c2d5f0a8ea7587ab3b2966021ccc: {e}")

if __name__ == "__main__":
    main()
