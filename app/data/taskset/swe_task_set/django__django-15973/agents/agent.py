import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('2480554dc4ada4ecf3f6a08e318735a2e50783f3')
        print(f"Checked out 2480554dc4ada4ecf3f6a08e318735a2e50783f3")
    except Exception as e:
        print(f"Failed to check out 2480554dc4ada4ecf3f6a08e318735a2e50783f3: {e}")

if __name__ == "__main__":
    main()
