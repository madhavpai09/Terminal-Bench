import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('278881e37619278789942513916acafaa88d26f3')
        print(f"Checked out 278881e37619278789942513916acafaa88d26f3")
    except Exception as e:
        print(f"Failed to check out 278881e37619278789942513916acafaa88d26f3: {e}")

if __name__ == "__main__":
    main()
