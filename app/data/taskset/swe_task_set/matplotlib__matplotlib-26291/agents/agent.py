import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('fa68f46289adf4a8a4bc7ba97ded8258ec9d079c')
        print(f"Checked out fa68f46289adf4a8a4bc7ba97ded8258ec9d079c")
    except Exception as e:
        print(f"Failed to check out fa68f46289adf4a8a4bc7ba97ded8258ec9d079c: {e}")

if __name__ == "__main__":
    main()
