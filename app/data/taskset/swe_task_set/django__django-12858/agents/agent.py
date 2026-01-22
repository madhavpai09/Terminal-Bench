import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('f2051eb8a7febdaaa43bd33bf5a6108c5f428e59')
        print(f"Checked out f2051eb8a7febdaaa43bd33bf5a6108c5f428e59")
    except Exception as e:
        print(f"Failed to check out f2051eb8a7febdaaa43bd33bf5a6108c5f428e59: {e}")

if __name__ == "__main__":
    main()
