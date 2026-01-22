import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('1e2ccd8f0eca0870cf6f8fce6934e2da8eba9b72')
        print(f"Checked out 1e2ccd8f0eca0870cf6f8fce6934e2da8eba9b72")
    except Exception as e:
        print(f"Failed to check out 1e2ccd8f0eca0870cf6f8fce6934e2da8eba9b72: {e}")

if __name__ == "__main__":
    main()
