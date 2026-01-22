import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('4b45b6c8e4d7c9701a332e80d3b1c84209dc36e2')
        print(f"Checked out 4b45b6c8e4d7c9701a332e80d3b1c84209dc36e2")
    except Exception as e:
        print(f"Failed to check out 4b45b6c8e4d7c9701a332e80d3b1c84209dc36e2: {e}")

if __name__ == "__main__":
    main()
