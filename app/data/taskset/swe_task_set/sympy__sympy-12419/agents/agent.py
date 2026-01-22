import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('479939f8c65c8c2908bbedc959549a257a7c0b0b')
        print(f"Checked out 479939f8c65c8c2908bbedc959549a257a7c0b0b")
    except Exception as e:
        print(f"Failed to check out 479939f8c65c8c2908bbedc959549a257a7c0b0b: {e}")

if __name__ == "__main__":
    main()
