import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('36367765fe780f962bba861bf368a765380bbc68')
        print(f"Checked out 36367765fe780f962bba861bf368a765380bbc68")
    except Exception as e:
        print(f"Failed to check out 36367765fe780f962bba861bf368a765380bbc68: {e}")

if __name__ == "__main__":
    main()
