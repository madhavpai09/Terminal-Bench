import os

def main(task_name, **kwargs):
    print(f"Task name: {task_name}")


def init_logger(task_name: str, log_level: Optional[int]=logging.INFO):
        log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
        os.makedirs(log_dir, exist_ok=True)
        
        logging.basicConfig(
            level=log_level,
            filename=os.path.join(log_dir, f"{task_name}.log"),
            filemode='w', 
            format=('%(asctime)s - %(levelname)s - %(message)s'))
        logger = logging.getLogger(task_name)
        return logger

if __name__ == "__main__":
    main("task_git_push")   