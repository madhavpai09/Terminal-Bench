import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('a5e6a101869e027e7930e694f8b1cfb082603453')
        print(f"Checked out a5e6a101869e027e7930e694f8b1cfb082603453")
    except Exception as e:
        print(f"Failed to check out a5e6a101869e027e7930e694f8b1cfb082603453: {e}")

if __name__ == "__main__":
    main()
