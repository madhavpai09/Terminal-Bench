import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('187118203197801c6cb72dc8b06b714b23b6dd3d')
        print(f"Checked out 187118203197801c6cb72dc8b06b714b23b6dd3d")
    except Exception as e:
        print(f"Failed to check out 187118203197801c6cb72dc8b06b714b23b6dd3d: {e}")

if __name__ == "__main__":
    main()
