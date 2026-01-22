import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/astropy/astropy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('fa4e8d1cd279acf9b24560813c8652494ccd5922')
        print(f"Checked out fa4e8d1cd279acf9b24560813c8652494ccd5922")
    except Exception as e:
        print(f"Failed to check out fa4e8d1cd279acf9b24560813c8652494ccd5922: {e}")

if __name__ == "__main__":
    main()
