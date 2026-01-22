import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('39f83765e12b0e5d260b7939fc3fe281d879b279')
        print(f"Checked out 39f83765e12b0e5d260b7939fc3fe281d879b279")
    except Exception as e:
        print(f"Failed to check out 39f83765e12b0e5d260b7939fc3fe281d879b279: {e}")

if __name__ == "__main__":
    main()
