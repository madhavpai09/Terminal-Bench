import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('6fd65310fa3167b9626c38a5487e171ca407d988')
        print(f"Checked out 6fd65310fa3167b9626c38a5487e171ca407d988")
    except Exception as e:
        print(f"Failed to check out 6fd65310fa3167b9626c38a5487e171ca407d988: {e}")

if __name__ == "__main__":
    main()
