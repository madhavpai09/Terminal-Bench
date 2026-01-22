import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('1923822ddf8265199dbd9ef9ce09641d3fd042b9')
        print(f"Checked out 1923822ddf8265199dbd9ef9ce09641d3fd042b9")
    except Exception as e:
        print(f"Failed to check out 1923822ddf8265199dbd9ef9ce09641d3fd042b9: {e}")

if __name__ == "__main__":
    main()
