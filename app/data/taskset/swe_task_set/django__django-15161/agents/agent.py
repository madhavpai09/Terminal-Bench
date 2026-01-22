import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('96e7ff5e9ff6362d9a886545869ce4496ca4b0fb')
        print(f"Checked out 96e7ff5e9ff6362d9a886545869ce4496ca4b0fb")
    except Exception as e:
        print(f"Failed to check out 96e7ff5e9ff6362d9a886545869ce4496ca4b0fb: {e}")

if __name__ == "__main__":
    main()
