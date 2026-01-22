import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('415f50298f97fb17f841a9df38d995ccf347dfcc')
        print(f"Checked out 415f50298f97fb17f841a9df38d995ccf347dfcc")
    except Exception as e:
        print(f"Failed to check out 415f50298f97fb17f841a9df38d995ccf347dfcc: {e}")

if __name__ == "__main__":
    main()
