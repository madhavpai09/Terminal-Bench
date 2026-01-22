import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('5d36a8266c7d5d1994d7a7eeb4016f80d9cb0401')
        print(f"Checked out 5d36a8266c7d5d1994d7a7eeb4016f80d9cb0401")
    except Exception as e:
        print(f"Failed to check out 5d36a8266c7d5d1994d7a7eeb4016f80d9cb0401: {e}")

if __name__ == "__main__":
    main()
