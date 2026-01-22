import git
import os

def gitclone(repo_url, target_dir):
    os.makedirs(target_dir, exist_ok=True)
    
    if os.path.exists(os.path.join(target_dir, '.git')):
        print(f"Repo already exists at {target_dir}")
        try:
            return git.Repo(target_dir)
        except git.exc.InvalidGitRepositoryError:
            print(f"Directory {target_dir} exists but is not a git repo. Removing and re-cloning.")
            import shutil
            shutil.rmtree(target_dir)
            os.makedirs(target_dir, exist_ok=True)
            
    print(f"Cloning {repo_url} to {target_dir}...")
    git.Git().clone(repo_url, target_dir)
    return git.Repo(target_dir)

