import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('e1d673c373a7d032060872b690a92fc95496612e')
        print(f"Checked out e1d673c373a7d032060872b690a92fc95496612e")
    except Exception as e:
        print(f"Failed to check out e1d673c373a7d032060872b690a92fc95496612e: {e}")

if __name__ == "__main__":
    main()
