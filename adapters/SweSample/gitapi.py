import git
import os

def clone_and_checkout(repo_url, target_dir, commit_hash):    
    os.makedirs(target_dir, exist_ok=True)

    repo = git.Repo.clone_from(repo_url, target_dir)
    repo.git.checkout(commit_hash)

