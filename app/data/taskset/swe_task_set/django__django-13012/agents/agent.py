import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('22a59c01c00cf9fbefaee0e8e67fab82bbaf1fd2')
        print(f"Checked out 22a59c01c00cf9fbefaee0e8e67fab82bbaf1fd2")
    except Exception as e:
        print(f"Failed to check out 22a59c01c00cf9fbefaee0e8e67fab82bbaf1fd2: {e}")

if __name__ == "__main__":
    main()
