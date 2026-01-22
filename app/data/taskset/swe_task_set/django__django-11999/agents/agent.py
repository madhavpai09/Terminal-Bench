import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('84633905273fc916e3d17883810d9969c03f73c2')
        print(f"Checked out 84633905273fc916e3d17883810d9969c03f73c2")
    except Exception as e:
        print(f"Failed to check out 84633905273fc916e3d17883810d9969c03f73c2: {e}")

if __name__ == "__main__":
    main()
