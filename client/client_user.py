import requests
from typing import Optional

def create_request(task_name):
    url = f"http://127.0.0.1:8000/create/{task_name}"
    response = requests.post(url)
    return response.json()
                 
def run_request():
    task_name="task_Hello_world"
    url = f"http://127.0.0.1:8000/run/{task_name}"
    response = requests.post(url)
    return response.json()

def send_request(
    request_type: str, 
    url_path: str, 
    params: Optional[dict],
    body: Optional[dict]
):
    if request_type == 'GET':
        response=requests.get(url_path)
        return response.json()
    elif request_type == 'POST':
        response=requests.post(url_path)
        return response.json()
    else:
        raise Exception(f"{request_type} not supported")
    
def main(task_name):
    result = send_request(request_type="POST",url_path=f"http://127.0.0.1:8000/run/{task_name}",params={1:1},body={1:1})
    print(result)

if __name__ == "__main__":
    main(task_name)