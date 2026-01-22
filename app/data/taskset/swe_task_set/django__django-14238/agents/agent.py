import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('30e123ed351317b7527f632b3b7dc4e81e850449')
        print(f"Checked out 30e123ed351317b7527f632b3b7dc4e81e850449")
    except Exception as e:
        print(f"Failed to check out 30e123ed351317b7527f632b3b7dc4e81e850449: {e}")

if __name__ == "__main__":
    main()
