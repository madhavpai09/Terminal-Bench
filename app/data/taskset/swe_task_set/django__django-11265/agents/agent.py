import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('21aa2a5e785eef1f47beb1c3760fdd7d8915ae09')
        print(f"Checked out 21aa2a5e785eef1f47beb1c3760fdd7d8915ae09")
    except Exception as e:
        print(f"Failed to check out 21aa2a5e785eef1f47beb1c3760fdd7d8915ae09: {e}")

if __name__ == "__main__":
    main()
