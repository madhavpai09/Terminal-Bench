import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('927c903f3cd25c817c21738328b53991c035b415')
        print(f"Checked out 927c903f3cd25c817c21738328b53991c035b415")
    except Exception as e:
        print(f"Failed to check out 927c903f3cd25c817c21738328b53991c035b415: {e}")

if __name__ == "__main__":
    main()
