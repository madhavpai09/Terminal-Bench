import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('2c7846d992ca512d36a73f518205015c88ed088c')
        print(f"Checked out 2c7846d992ca512d36a73f518205015c88ed088c")
    except Exception as e:
        print(f"Failed to check out 2c7846d992ca512d36a73f518205015c88ed088c: {e}")

if __name__ == "__main__":
    main()
