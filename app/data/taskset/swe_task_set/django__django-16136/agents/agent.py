import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('19e6efa50b603af325e7f62058364f278596758f')
        print(f"Checked out 19e6efa50b603af325e7f62058364f278596758f")
    except Exception as e:
        print(f"Failed to check out 19e6efa50b603af325e7f62058364f278596758f: {e}")

if __name__ == "__main__":
    main()
