import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('9a6e2df3a8f01ea761529bec48e5a8dc0ea9575b')
        print(f"Checked out 9a6e2df3a8f01ea761529bec48e5a8dc0ea9575b")
    except Exception as e:
        print(f"Failed to check out 9a6e2df3a8f01ea761529bec48e5a8dc0ea9575b: {e}")

if __name__ == "__main__":
    main()
