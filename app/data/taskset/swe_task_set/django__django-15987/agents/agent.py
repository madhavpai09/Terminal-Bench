import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('7e6b537f5b92be152779fc492bb908d27fe7c52a')
        print(f"Checked out 7e6b537f5b92be152779fc492bb908d27fe7c52a")
    except Exception as e:
        print(f"Failed to check out 7e6b537f5b92be152779fc492bb908d27fe7c52a: {e}")

if __name__ == "__main__":
    main()
