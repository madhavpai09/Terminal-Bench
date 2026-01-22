import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('6866c91b638de5368c18713fa851bfe56253ea55')
        print(f"Checked out 6866c91b638de5368c18713fa851bfe56253ea55")
    except Exception as e:
        print(f"Failed to check out 6866c91b638de5368c18713fa851bfe56253ea55: {e}")

if __name__ == "__main__":
    main()
