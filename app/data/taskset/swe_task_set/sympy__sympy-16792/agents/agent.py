import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('09786a173e7a0a488f46dd6000177c23e5d24eed')
        print(f"Checked out 09786a173e7a0a488f46dd6000177c23e5d24eed")
    except Exception as e:
        print(f"Failed to check out 09786a173e7a0a488f46dd6000177c23e5d24eed: {e}")

if __name__ == "__main__":
    main()
