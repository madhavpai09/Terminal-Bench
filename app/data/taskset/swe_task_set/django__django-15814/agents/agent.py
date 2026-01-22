import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('5eb6a2b33d70b9889e1cafa12594ad6f80773d3a')
        print(f"Checked out 5eb6a2b33d70b9889e1cafa12594ad6f80773d3a")
    except Exception as e:
        print(f"Failed to check out 5eb6a2b33d70b9889e1cafa12594ad6f80773d3a: {e}")

if __name__ == "__main__":
    main()
