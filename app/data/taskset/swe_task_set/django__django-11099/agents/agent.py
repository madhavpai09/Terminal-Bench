import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('d26b2424437dabeeca94d7900b37d2df4410da0c')
        print(f"Checked out d26b2424437dabeeca94d7900b37d2df4410da0c")
    except Exception as e:
        print(f"Failed to check out d26b2424437dabeeca94d7900b37d2df4410da0c: {e}")

if __name__ == "__main__":
    main()
