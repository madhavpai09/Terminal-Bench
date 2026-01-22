import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('b7da588e883e12b8ac3bb8a486e654e30fc1c6c8')
        print(f"Checked out b7da588e883e12b8ac3bb8a486e654e30fc1c6c8")
    except Exception as e:
        print(f"Failed to check out b7da588e883e12b8ac3bb8a486e654e30fc1c6c8: {e}")

if __name__ == "__main__":
    main()
