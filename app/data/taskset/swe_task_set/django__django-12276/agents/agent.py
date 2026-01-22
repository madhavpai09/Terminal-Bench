import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('53d8646f799de7f92ab9defe9dc56c6125448102')
        print(f"Checked out 53d8646f799de7f92ab9defe9dc56c6125448102")
    except Exception as e:
        print(f"Failed to check out 53d8646f799de7f92ab9defe9dc56c6125448102: {e}")

if __name__ == "__main__":
    main()
