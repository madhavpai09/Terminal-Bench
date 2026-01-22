import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('2d67222472f80f251607ae1b720527afceba06ad')
        print(f"Checked out 2d67222472f80f251607ae1b720527afceba06ad")
    except Exception as e:
        print(f"Failed to check out 2d67222472f80f251607ae1b720527afceba06ad: {e}")

if __name__ == "__main__":
    main()
