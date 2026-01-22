import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('f7eea978097085a6781a0e92fc14ba7712a52d75')
        print(f"Checked out f7eea978097085a6781a0e92fc14ba7712a52d75")
    except Exception as e:
        print(f"Failed to check out f7eea978097085a6781a0e92fc14ba7712a52d75: {e}")

if __name__ == "__main__":
    main()
