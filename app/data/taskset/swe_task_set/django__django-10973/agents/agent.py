import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('ddb293685235fd09e932805771ae97f72e817181')
        print(f"Checked out ddb293685235fd09e932805771ae97f72e817181")
    except Exception as e:
        print(f"Failed to check out ddb293685235fd09e932805771ae97f72e817181: {e}")

if __name__ == "__main__":
    main()
