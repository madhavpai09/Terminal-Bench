import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('2a55431a5678af52f669ffe7dff3dd0bd21727f8')
        print(f"Checked out 2a55431a5678af52f669ffe7dff3dd0bd21727f8")
    except Exception as e:
        print(f"Failed to check out 2a55431a5678af52f669ffe7dff3dd0bd21727f8: {e}")

if __name__ == "__main__":
    main()
