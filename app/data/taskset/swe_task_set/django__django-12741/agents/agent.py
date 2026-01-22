import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('537d422942b53bc0a2b6a51968f379c0de07793c')
        print(f"Checked out 537d422942b53bc0a2b6a51968f379c0de07793c")
    except Exception as e:
        print(f"Failed to check out 537d422942b53bc0a2b6a51968f379c0de07793c: {e}")

if __name__ == "__main__":
    main()
