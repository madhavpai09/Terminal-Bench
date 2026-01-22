import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('335c9c94acf263901fb023404408880245b0c4b4')
        print(f"Checked out 335c9c94acf263901fb023404408880245b0c4b4")
    except Exception as e:
        print(f"Failed to check out 335c9c94acf263901fb023404408880245b0c4b4: {e}")

if __name__ == "__main__":
    main()
