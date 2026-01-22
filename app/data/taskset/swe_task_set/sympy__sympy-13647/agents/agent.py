import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('67e3c956083d0128a621f65ee86a7dacd4f9f19f')
        print(f"Checked out 67e3c956083d0128a621f65ee86a7dacd4f9f19f")
    except Exception as e:
        print(f"Failed to check out 67e3c956083d0128a621f65ee86a7dacd4f9f19f: {e}")

if __name__ == "__main__":
    main()
