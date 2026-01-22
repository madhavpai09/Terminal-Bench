import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('110997fe18b9f7d5ba7d22f624d156a29bf40759')
        print(f"Checked out 110997fe18b9f7d5ba7d22f624d156a29bf40759")
    except Exception as e:
        print(f"Failed to check out 110997fe18b9f7d5ba7d22f624d156a29bf40759: {e}")

if __name__ == "__main__":
    main()
