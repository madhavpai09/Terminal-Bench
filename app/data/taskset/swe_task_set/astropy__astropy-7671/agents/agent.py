import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/astropy/astropy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('a7141cd90019b62688d507ae056298507678c058')
        print(f"Checked out a7141cd90019b62688d507ae056298507678c058")
    except Exception as e:
        print(f"Failed to check out a7141cd90019b62688d507ae056298507678c058: {e}")

if __name__ == "__main__":
    main()
