import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('36300ef336e3f130a0dadc1143163ff3d23dc843')
        print(f"Checked out 36300ef336e3f130a0dadc1143163ff3d23dc843")
    except Exception as e:
        print(f"Failed to check out 36300ef336e3f130a0dadc1143163ff3d23dc843: {e}")

if __name__ == "__main__":
    main()
