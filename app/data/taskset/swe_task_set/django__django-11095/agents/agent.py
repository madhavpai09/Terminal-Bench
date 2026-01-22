import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('7d49ad76562e8c0597a0eb66046ab423b12888d8')
        print(f"Checked out 7d49ad76562e8c0597a0eb66046ab423b12888d8")
    except Exception as e:
        print(f"Failed to check out 7d49ad76562e8c0597a0eb66046ab423b12888d8: {e}")

if __name__ == "__main__":
    main()
