import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('d559cb02da30f74debbb1fc3a46de0df134d2d80')
        print(f"Checked out d559cb02da30f74debbb1fc3a46de0df134d2d80")
    except Exception as e:
        print(f"Failed to check out d559cb02da30f74debbb1fc3a46de0df134d2d80: {e}")

if __name__ == "__main__":
    main()
