import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('30379ea6e225e37833a764ac2da7b7fadf5fe374')
        print(f"Checked out 30379ea6e225e37833a764ac2da7b7fadf5fe374")
    except Exception as e:
        print(f"Failed to check out 30379ea6e225e37833a764ac2da7b7fadf5fe374: {e}")

if __name__ == "__main__":
    main()
