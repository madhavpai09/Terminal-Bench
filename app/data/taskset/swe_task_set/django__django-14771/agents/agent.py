import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('4884a87e022056eda10534c13d74e49b8cdda632')
        print(f"Checked out 4884a87e022056eda10534c13d74e49b8cdda632")
    except Exception as e:
        print(f"Failed to check out 4884a87e022056eda10534c13d74e49b8cdda632: {e}")

if __name__ == "__main__":
    main()
