import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('84400d2e9db7c51fee4e9bb04c028f665b8e7624')
        print(f"Checked out 84400d2e9db7c51fee4e9bb04c028f665b8e7624")
    except Exception as e:
        print(f"Failed to check out 84400d2e9db7c51fee4e9bb04c028f665b8e7624: {e}")

if __name__ == "__main__":
    main()
