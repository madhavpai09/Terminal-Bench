import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('701441853569d370506514083b995d11f9a130bd')
        print(f"Checked out 701441853569d370506514083b995d11f9a130bd")
    except Exception as e:
        print(f"Failed to check out 701441853569d370506514083b995d11f9a130bd: {e}")

if __name__ == "__main__":
    main()
