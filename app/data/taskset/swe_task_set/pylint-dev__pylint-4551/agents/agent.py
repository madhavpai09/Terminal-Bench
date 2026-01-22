import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pylint-dev/pylint"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('99589b08de8c5a2c6cc61e13a37420a868c80599')
        print(f"Checked out 99589b08de8c5a2c6cc61e13a37420a868c80599")
    except Exception as e:
        print(f"Failed to check out 99589b08de8c5a2c6cc61e13a37420a868c80599: {e}")

if __name__ == "__main__":
    main()
