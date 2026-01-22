import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('bd366ca2aeffa869b7dbc0b0aa01caea75e6dc31')
        print(f"Checked out bd366ca2aeffa869b7dbc0b0aa01caea75e6dc31")
    except Exception as e:
        print(f"Failed to check out bd366ca2aeffa869b7dbc0b0aa01caea75e6dc31: {e}")

if __name__ == "__main__":
    main()
