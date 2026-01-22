import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('939c7bb7ff7c53a4d27df067cea637540f0e1dad')
        print(f"Checked out 939c7bb7ff7c53a4d27df067cea637540f0e1dad")
    except Exception as e:
        print(f"Failed to check out 939c7bb7ff7c53a4d27df067cea637540f0e1dad: {e}")

if __name__ == "__main__":
    main()
