import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('a36caf5c74fe654cedc488e8a8a05fad388f8406')
        print(f"Checked out a36caf5c74fe654cedc488e8a8a05fad388f8406")
    except Exception as e:
        print(f"Failed to check out a36caf5c74fe654cedc488e8a8a05fad388f8406: {e}")

if __name__ == "__main__":
    main()
