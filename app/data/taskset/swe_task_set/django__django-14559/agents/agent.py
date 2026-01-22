import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('d79be3ed39b76d3e34431873eec16f6dd354ab17')
        print(f"Checked out d79be3ed39b76d3e34431873eec16f6dd354ab17")
    except Exception as e:
        print(f"Failed to check out d79be3ed39b76d3e34431873eec16f6dd354ab17: {e}")

if __name__ == "__main__":
    main()
