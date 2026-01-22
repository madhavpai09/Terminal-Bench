import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('f39634ff229887bf7790c069d0c411b38494ca38')
        print(f"Checked out f39634ff229887bf7790c069d0c411b38494ca38")
    except Exception as e:
        print(f"Failed to check out f39634ff229887bf7790c069d0c411b38494ca38: {e}")

if __name__ == "__main__":
    main()
