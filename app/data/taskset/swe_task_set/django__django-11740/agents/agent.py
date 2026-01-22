import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('003bb34b218adb23d1a7e67932a6ba9b3c4dcc81')
        print(f"Checked out 003bb34b218adb23d1a7e67932a6ba9b3c4dcc81")
    except Exception as e:
        print(f"Failed to check out 003bb34b218adb23d1a7e67932a6ba9b3c4dcc81: {e}")

if __name__ == "__main__":
    main()
