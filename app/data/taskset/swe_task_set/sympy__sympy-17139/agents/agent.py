import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('1d3327b8e90a186df6972991963a5ae87053259d')
        print(f"Checked out 1d3327b8e90a186df6972991963a5ae87053259d")
    except Exception as e:
        print(f"Failed to check out 1d3327b8e90a186df6972991963a5ae87053259d: {e}")

if __name__ == "__main__":
    main()
