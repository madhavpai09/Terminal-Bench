import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('7272e1963ffdf39c1d4fe225d5425a45dd095d11')
        print(f"Checked out 7272e1963ffdf39c1d4fe225d5425a45dd095d11")
    except Exception as e:
        print(f"Failed to check out 7272e1963ffdf39c1d4fe225d5425a45dd095d11: {e}")

if __name__ == "__main__":
    main()
