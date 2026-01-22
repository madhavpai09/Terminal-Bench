import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('d9b18c518d64d0ebe8e35a98c2fb519938b9b151')
        print(f"Checked out d9b18c518d64d0ebe8e35a98c2fb519938b9b151")
    except Exception as e:
        print(f"Failed to check out d9b18c518d64d0ebe8e35a98c2fb519938b9b151: {e}")

if __name__ == "__main__":
    main()
