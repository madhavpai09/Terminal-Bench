import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('d89f976bddb49fb168334960acc8979c3de991fa')
        print(f"Checked out d89f976bddb49fb168334960acc8979c3de991fa")
    except Exception as e:
        print(f"Failed to check out d89f976bddb49fb168334960acc8979c3de991fa: {e}")

if __name__ == "__main__":
    main()
