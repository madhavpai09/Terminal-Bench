import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('7991111af12056ec9a856f35935d273526338c1f')
        print(f"Checked out 7991111af12056ec9a856f35935d273526338c1f")
    except Exception as e:
        print(f"Failed to check out 7991111af12056ec9a856f35935d273526338c1f: {e}")

if __name__ == "__main__":
    main()
