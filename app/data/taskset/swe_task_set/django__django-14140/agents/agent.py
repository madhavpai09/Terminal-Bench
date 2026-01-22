import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('45814af6197cfd8f4dc72ee43b90ecde305a1d5a')
        print(f"Checked out 45814af6197cfd8f4dc72ee43b90ecde305a1d5a")
    except Exception as e:
        print(f"Failed to check out 45814af6197cfd8f4dc72ee43b90ecde305a1d5a: {e}")

if __name__ == "__main__":
    main()
