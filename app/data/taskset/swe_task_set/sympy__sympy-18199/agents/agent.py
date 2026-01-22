import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('ba80d1e493f21431b4bf729b3e0452cd47eb9566')
        print(f"Checked out ba80d1e493f21431b4bf729b3e0452cd47eb9566")
    except Exception as e:
        print(f"Failed to check out ba80d1e493f21431b4bf729b3e0452cd47eb9566: {e}")

if __name__ == "__main__":
    main()
