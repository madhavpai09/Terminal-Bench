import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('321ecb40f4da842926e1bc07e11df4aabe53ca4b')
        print(f"Checked out 321ecb40f4da842926e1bc07e11df4aabe53ca4b")
    except Exception as e:
        print(f"Failed to check out 321ecb40f4da842926e1bc07e11df4aabe53ca4b: {e}")

if __name__ == "__main__":
    main()
