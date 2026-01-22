import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('b64db05b9cedd96905d637a2d824cbbf428e40e7')
        print(f"Checked out b64db05b9cedd96905d637a2d824cbbf428e40e7")
    except Exception as e:
        print(f"Failed to check out b64db05b9cedd96905d637a2d824cbbf428e40e7: {e}")

if __name__ == "__main__":
    main()
