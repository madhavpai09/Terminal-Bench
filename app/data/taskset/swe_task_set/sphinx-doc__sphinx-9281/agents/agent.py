import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('8ec06e9a1bd862cd713b9db748e039ccc7b3e15b')
        print(f"Checked out 8ec06e9a1bd862cd713b9db748e039ccc7b3e15b")
    except Exception as e:
        print(f"Failed to check out 8ec06e9a1bd862cd713b9db748e039ccc7b3e15b: {e}")

if __name__ == "__main__":
    main()
