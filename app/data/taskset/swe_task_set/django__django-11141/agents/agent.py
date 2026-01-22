import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('5d9cf79baf07fc4aed7ad1b06990532a65378155')
        print(f"Checked out 5d9cf79baf07fc4aed7ad1b06990532a65378155")
    except Exception as e:
        print(f"Failed to check out 5d9cf79baf07fc4aed7ad1b06990532a65378155: {e}")

if __name__ == "__main__":
    main()
