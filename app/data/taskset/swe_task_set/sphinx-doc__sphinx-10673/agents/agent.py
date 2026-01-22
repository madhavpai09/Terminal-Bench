import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('f35d2a6cc726f97d0e859ca7a0e1729f7da8a6c8')
        print(f"Checked out f35d2a6cc726f97d0e859ca7a0e1729f7da8a6c8")
    except Exception as e:
        print(f"Failed to check out f35d2a6cc726f97d0e859ca7a0e1729f7da8a6c8: {e}")

if __name__ == "__main__":
    main()
