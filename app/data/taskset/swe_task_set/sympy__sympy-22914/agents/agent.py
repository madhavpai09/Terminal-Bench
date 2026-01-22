import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('c4e836cdf73fc6aa7bab6a86719a0f08861ffb1d')
        print(f"Checked out c4e836cdf73fc6aa7bab6a86719a0f08861ffb1d")
    except Exception as e:
        print(f"Failed to check out c4e836cdf73fc6aa7bab6a86719a0f08861ffb1d: {e}")

if __name__ == "__main__":
    main()
