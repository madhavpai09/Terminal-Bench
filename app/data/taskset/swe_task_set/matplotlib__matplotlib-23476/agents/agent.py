import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('33a0599711d26dc2b79f851c6daed4947df7c167')
        print(f"Checked out 33a0599711d26dc2b79f851c6daed4947df7c167")
    except Exception as e:
        print(f"Failed to check out 33a0599711d26dc2b79f851c6daed4947df7c167: {e}")

if __name__ == "__main__":
    main()
