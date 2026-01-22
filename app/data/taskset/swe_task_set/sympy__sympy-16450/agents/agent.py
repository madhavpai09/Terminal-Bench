import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('aefdd023dc4f73c441953ed51f5f05a076f0862f')
        print(f"Checked out aefdd023dc4f73c441953ed51f5f05a076f0862f")
    except Exception as e:
        print(f"Failed to check out aefdd023dc4f73c441953ed51f5f05a076f0862f: {e}")

if __name__ == "__main__":
    main()
