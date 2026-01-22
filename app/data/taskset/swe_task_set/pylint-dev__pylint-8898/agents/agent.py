import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pylint-dev/pylint"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('1f8c4d9eb185c16a2c1d881c054f015e1c2eb334')
        print(f"Checked out 1f8c4d9eb185c16a2c1d881c054f015e1c2eb334")
    except Exception as e:
        print(f"Failed to check out 1f8c4d9eb185c16a2c1d881c054f015e1c2eb334: {e}")

if __name__ == "__main__":
    main()
