import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('50d8a102f0735da8e165a0369bbb994c7d0592a6')
        print(f"Checked out 50d8a102f0735da8e165a0369bbb994c7d0592a6")
    except Exception as e:
        print(f"Failed to check out 50d8a102f0735da8e165a0369bbb994c7d0592a6: {e}")

if __name__ == "__main__":
    main()
