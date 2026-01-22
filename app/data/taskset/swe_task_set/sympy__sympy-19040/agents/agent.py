import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('b9179e80d2daa1bb6cba1ffe35ca9e6612e115c9')
        print(f"Checked out b9179e80d2daa1bb6cba1ffe35ca9e6612e115c9")
    except Exception as e:
        print(f"Failed to check out b9179e80d2daa1bb6cba1ffe35ca9e6612e115c9: {e}")

if __name__ == "__main__":
    main()
