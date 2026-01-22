import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/astropy/astropy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('6500928dc0e57be8f06d1162eacc3ba5e2eff692')
        print(f"Checked out 6500928dc0e57be8f06d1162eacc3ba5e2eff692")
    except Exception as e:
        print(f"Failed to check out 6500928dc0e57be8f06d1162eacc3ba5e2eff692: {e}")

if __name__ == "__main__":
    main()
