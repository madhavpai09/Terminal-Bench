import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('60a7bd89860e504c0c33b02c78edcac87f6d1b5a')
        print(f"Checked out 60a7bd89860e504c0c33b02c78edcac87f6d1b5a")
    except Exception as e:
        print(f"Failed to check out 60a7bd89860e504c0c33b02c78edcac87f6d1b5a: {e}")

if __name__ == "__main__":
    main()
