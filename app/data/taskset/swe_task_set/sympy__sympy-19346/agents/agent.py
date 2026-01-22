import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('94fb720696f5f5d12bad8bc813699fd696afd2fb')
        print(f"Checked out 94fb720696f5f5d12bad8bc813699fd696afd2fb")
    except Exception as e:
        print(f"Failed to check out 94fb720696f5f5d12bad8bc813699fd696afd2fb: {e}")

if __name__ == "__main__":
    main()
