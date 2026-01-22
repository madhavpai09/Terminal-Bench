import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('004b4620f6f4ad87261e149898940f2dcd5757ef')
        print(f"Checked out 004b4620f6f4ad87261e149898940f2dcd5757ef")
    except Exception as e:
        print(f"Failed to check out 004b4620f6f4ad87261e149898940f2dcd5757ef: {e}")

if __name__ == "__main__":
    main()
