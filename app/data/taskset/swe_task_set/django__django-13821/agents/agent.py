import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('e64c1d8055a3e476122633da141f16b50f0c4a2d')
        print(f"Checked out e64c1d8055a3e476122633da141f16b50f0c4a2d")
    except Exception as e:
        print(f"Failed to check out e64c1d8055a3e476122633da141f16b50f0c4a2d: {e}")

if __name__ == "__main__":
    main()
