import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('fdc707f73a65a429935c01532cd3970d3355eab6')
        print(f"Checked out fdc707f73a65a429935c01532cd3970d3355eab6")
    except Exception as e:
        print(f"Failed to check out fdc707f73a65a429935c01532cd3970d3355eab6: {e}")

if __name__ == "__main__":
    main()
