import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('fbe82f82555bc25dccb476c749ca062f0b522be3')
        print(f"Checked out fbe82f82555bc25dccb476c749ca062f0b522be3")
    except Exception as e:
        print(f"Failed to check out fbe82f82555bc25dccb476c749ca062f0b522be3: {e}")

if __name__ == "__main__":
    main()
