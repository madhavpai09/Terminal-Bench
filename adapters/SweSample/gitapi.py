import git
import os

def gitclone(repo_url, target_dir):
    os.makedirs(target_dir, exist_ok=True)
            
    print(f"Cloning {repo_url} to {target_dir}...")
    git.Git().clone(repo_url, target_dir)
    return git.Repo(target_dir)

