import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('f0632c0fc7339f68e992ed63ae4cfac76cd41aad')
        print(f"Checked out f0632c0fc7339f68e992ed63ae4cfac76cd41aad")
    except Exception as e:
        print(f"Failed to check out f0632c0fc7339f68e992ed63ae4cfac76cd41aad: {e}")

if __name__ == "__main__":
    main()
