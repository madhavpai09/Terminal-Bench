import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('694cf458f16b8d340a3195244196980b2dec34fd')
        print(f"Checked out 694cf458f16b8d340a3195244196980b2dec34fd")
    except Exception as e:
        print(f"Failed to check out 694cf458f16b8d340a3195244196980b2dec34fd: {e}")

if __name__ == "__main__":
    main()
