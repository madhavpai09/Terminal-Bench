import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('31eba1a76dd485dc633cae48227b46879eda5df4')
        print(f"Checked out 31eba1a76dd485dc633cae48227b46879eda5df4")
    except Exception as e:
        print(f"Failed to check out 31eba1a76dd485dc633cae48227b46879eda5df4: {e}")

if __name__ == "__main__":
    main()
