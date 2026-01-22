import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('05457817647368be4b019314fcc655445a5b4c0c')
        print(f"Checked out 05457817647368be4b019314fcc655445a5b4c0c")
    except Exception as e:
        print(f"Failed to check out 05457817647368be4b019314fcc655445a5b4c0c: {e}")

if __name__ == "__main__":
    main()
