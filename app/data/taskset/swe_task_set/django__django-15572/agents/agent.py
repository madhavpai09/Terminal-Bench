import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('0b31e024873681e187b574fe1c4afe5e48aeeecf')
        print(f"Checked out 0b31e024873681e187b574fe1c4afe5e48aeeecf")
    except Exception as e:
        print(f"Failed to check out 0b31e024873681e187b574fe1c4afe5e48aeeecf: {e}")

if __name__ == "__main__":
    main()
