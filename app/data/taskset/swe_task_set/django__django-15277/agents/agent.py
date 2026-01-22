import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('30613d6a748fce18919ff8b0da166d9fda2ed9bc')
        print(f"Checked out 30613d6a748fce18919ff8b0da166d9fda2ed9bc")
    except Exception as e:
        print(f"Failed to check out 30613d6a748fce18919ff8b0da166d9fda2ed9bc: {e}")

if __name__ == "__main__":
    main()
