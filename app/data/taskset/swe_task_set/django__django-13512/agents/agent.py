import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('b79088306513d5ed76d31ac40ab3c15f858946ea')
        print(f"Checked out b79088306513d5ed76d31ac40ab3c15f858946ea")
    except Exception as e:
        print(f"Failed to check out b79088306513d5ed76d31ac40ab3c15f858946ea: {e}")

if __name__ == "__main__":
    main()
