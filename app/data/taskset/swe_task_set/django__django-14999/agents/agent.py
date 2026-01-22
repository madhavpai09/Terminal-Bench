import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('a754b82dac511475b6276039471ccd17cc64aeb8')
        print(f"Checked out a754b82dac511475b6276039471ccd17cc64aeb8")
    except Exception as e:
        print(f"Failed to check out a754b82dac511475b6276039471ccd17cc64aeb8: {e}")

if __name__ == "__main__":
    main()
