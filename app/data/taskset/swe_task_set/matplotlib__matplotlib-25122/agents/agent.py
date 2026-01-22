import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('5ec2bd279729ff534719b8bf238dbbca907b93c5')
        print(f"Checked out 5ec2bd279729ff534719b8bf238dbbca907b93c5")
    except Exception as e:
        print(f"Failed to check out 5ec2bd279729ff534719b8bf238dbbca907b93c5: {e}")

if __name__ == "__main__":
    main()
