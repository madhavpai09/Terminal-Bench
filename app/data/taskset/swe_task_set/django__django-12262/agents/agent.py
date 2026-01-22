import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('69331bb851c34f05bc77e9fc24020fe6908b9cd5')
        print(f"Checked out 69331bb851c34f05bc77e9fc24020fe6908b9cd5")
    except Exception as e:
        print(f"Failed to check out 69331bb851c34f05bc77e9fc24020fe6908b9cd5: {e}")

if __name__ == "__main__":
    main()
