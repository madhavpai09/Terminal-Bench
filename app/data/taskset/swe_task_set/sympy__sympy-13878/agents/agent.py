import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('7b127bdf71a36d85216315f80c1b54d22b060818')
        print(f"Checked out 7b127bdf71a36d85216315f80c1b54d22b060818")
    except Exception as e:
        print(f"Failed to check out 7b127bdf71a36d85216315f80c1b54d22b060818: {e}")

if __name__ == "__main__":
    main()
