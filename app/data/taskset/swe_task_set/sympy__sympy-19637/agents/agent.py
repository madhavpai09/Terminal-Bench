import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('63f8f465d48559fecb4e4bf3c48b75bf15a3e0ef')
        print(f"Checked out 63f8f465d48559fecb4e4bf3c48b75bf15a3e0ef")
    except Exception as e:
        print(f"Failed to check out 63f8f465d48559fecb4e4bf3c48b75bf15a3e0ef: {e}")

if __name__ == "__main__":
    main()
