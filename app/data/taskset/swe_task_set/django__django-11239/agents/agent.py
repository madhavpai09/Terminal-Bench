import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('d87bd29c4f8dfcdf3f4a4eb8340e6770a2416fe3')
        print(f"Checked out d87bd29c4f8dfcdf3f4a4eb8340e6770a2416fe3")
    except Exception as e:
        print(f"Failed to check out d87bd29c4f8dfcdf3f4a4eb8340e6770a2416fe3: {e}")

if __name__ == "__main__":
    main()
