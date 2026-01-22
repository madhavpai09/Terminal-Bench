import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('755dbf39fcdc491fe9b588358303e259c7750be4')
        print(f"Checked out 755dbf39fcdc491fe9b588358303e259c7750be4")
    except Exception as e:
        print(f"Failed to check out 755dbf39fcdc491fe9b588358303e259c7750be4: {e}")

if __name__ == "__main__":
    main()
