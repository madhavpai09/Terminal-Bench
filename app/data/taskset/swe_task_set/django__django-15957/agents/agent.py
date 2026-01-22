import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('f387d024fc75569d2a4a338bfda76cc2f328f627')
        print(f"Checked out f387d024fc75569d2a4a338bfda76cc2f328f627")
    except Exception as e:
        print(f"Failed to check out f387d024fc75569d2a4a338bfda76cc2f328f627: {e}")

if __name__ == "__main__":
    main()
