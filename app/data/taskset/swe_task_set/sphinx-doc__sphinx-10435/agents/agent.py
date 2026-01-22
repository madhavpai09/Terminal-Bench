import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('f1061c012e214f16fd8790dec3c283d787e3daa8')
        print(f"Checked out f1061c012e214f16fd8790dec3c283d787e3daa8")
    except Exception as e:
        print(f"Failed to check out f1061c012e214f16fd8790dec3c283d787e3daa8: {e}")

if __name__ == "__main__":
    main()
