import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('33b47e4bd60e2302e42616141e76285038b724d6')
        print(f"Checked out 33b47e4bd60e2302e42616141e76285038b724d6")
    except Exception as e:
        print(f"Failed to check out 33b47e4bd60e2302e42616141e76285038b724d6: {e}")

if __name__ == "__main__":
    main()
