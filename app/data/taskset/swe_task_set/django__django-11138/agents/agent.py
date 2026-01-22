import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('c84b91b7603e488f7171fdff8f08368ef3d6b856')
        print(f"Checked out c84b91b7603e488f7171fdff8f08368ef3d6b856")
    except Exception as e:
        print(f"Failed to check out c84b91b7603e488f7171fdff8f08368ef3d6b856: {e}")

if __name__ == "__main__":
    main()
