import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('9476425b9e34363c2d9ac38e9f04aa75ae54a775')
        print(f"Checked out 9476425b9e34363c2d9ac38e9f04aa75ae54a775")
    except Exception as e:
        print(f"Failed to check out 9476425b9e34363c2d9ac38e9f04aa75ae54a775: {e}")

if __name__ == "__main__":
    main()
