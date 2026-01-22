import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pylint-dev/pylint"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('40cc2ffd7887959157aaf469e09585ec2be7f528')
        print(f"Checked out 40cc2ffd7887959157aaf469e09585ec2be7f528")
    except Exception as e:
        print(f"Failed to check out 40cc2ffd7887959157aaf469e09585ec2be7f528: {e}")

if __name__ == "__main__":
    main()
