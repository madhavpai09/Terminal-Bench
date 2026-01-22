import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('514579c655bf22e2af14f0743376ae1d7befe345')
        print(f"Checked out 514579c655bf22e2af14f0743376ae1d7befe345")
    except Exception as e:
        print(f"Failed to check out 514579c655bf22e2af14f0743376ae1d7befe345: {e}")

if __name__ == "__main__":
    main()
