import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/psf/requests"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('847735553aeda6e6633f2b32e14ba14ba86887a4')
        print(f"Checked out 847735553aeda6e6633f2b32e14ba14ba86887a4")
    except Exception as e:
        print(f"Failed to check out 847735553aeda6e6633f2b32e14ba14ba86887a4: {e}")

if __name__ == "__main__":
    main()
