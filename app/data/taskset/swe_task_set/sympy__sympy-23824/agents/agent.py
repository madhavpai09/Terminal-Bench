import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('39de9a2698ad4bb90681c0fdb70b30a78233145f')
        print(f"Checked out 39de9a2698ad4bb90681c0fdb70b30a78233145f")
    except Exception as e:
        print(f"Failed to check out 39de9a2698ad4bb90681c0fdb70b30a78233145f: {e}")

if __name__ == "__main__":
    main()
