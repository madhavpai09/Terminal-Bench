import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('c2678e49759e5c4c329bff0eeca2886267005d21')
        print(f"Checked out c2678e49759e5c4c329bff0eeca2886267005d21")
    except Exception as e:
        print(f"Failed to check out c2678e49759e5c4c329bff0eeca2886267005d21: {e}")

if __name__ == "__main__":
    main()
