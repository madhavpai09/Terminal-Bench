import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/astropy/astropy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('732d89c2940156bdc0e200bb36dc38b5e424bcba')
        print(f"Checked out 732d89c2940156bdc0e200bb36dc38b5e424bcba")
    except Exception as e:
        print(f"Failed to check out 732d89c2940156bdc0e200bb36dc38b5e424bcba: {e}")

if __name__ == "__main__":
    main()
