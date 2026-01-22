import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('0b0998dc151feb77068e2387c34cc50ef6b356ae')
        print(f"Checked out 0b0998dc151feb77068e2387c34cc50ef6b356ae")
    except Exception as e:
        print(f"Failed to check out 0b0998dc151feb77068e2387c34cc50ef6b356ae: {e}")

if __name__ == "__main__":
    main()
