import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/astropy/astropy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('80c3854a5f4f4a6ab86c03d9db7854767fcd83c1')
        print(f"Checked out 80c3854a5f4f4a6ab86c03d9db7854767fcd83c1")
    except Exception as e:
        print(f"Failed to check out 80c3854a5f4f4a6ab86c03d9db7854767fcd83c1: {e}")

if __name__ == "__main__":
    main()
