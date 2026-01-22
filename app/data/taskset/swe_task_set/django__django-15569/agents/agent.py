import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('884b4c27f506b3c29d58509fc83a35c30ea10d94')
        print(f"Checked out 884b4c27f506b3c29d58509fc83a35c30ea10d94")
    except Exception as e:
        print(f"Failed to check out 884b4c27f506b3c29d58509fc83a35c30ea10d94: {e}")

if __name__ == "__main__":
    main()
