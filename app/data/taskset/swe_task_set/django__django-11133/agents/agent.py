import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('879cc3da6249e920b8d54518a0ae06de835d7373')
        print(f"Checked out 879cc3da6249e920b8d54518a0ae06de835d7373")
    except Exception as e:
        print(f"Failed to check out 879cc3da6249e920b8d54518a0ae06de835d7373: {e}")

if __name__ == "__main__":
    main()
