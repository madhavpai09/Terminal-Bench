import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('a5308514fb4bc5086c9a16a8a24a945eeebb073c')
        print(f"Checked out a5308514fb4bc5086c9a16a8a24a945eeebb073c")
    except Exception as e:
        print(f"Failed to check out a5308514fb4bc5086c9a16a8a24a945eeebb073c: {e}")

if __name__ == "__main__":
    main()
