import requests
from typing import Optional
import sys

def create_request(task_name):
    url = f"http://127.0.0.1:8000/create/{task_name}"
    response = requests.post(url)
    return response.json()
                 
def run_request():
    task_name = "task_Hello_world"
    url = f"http://127.0.0.1:8000/run/{task_name}"
    response = requests.post(url)
    return response.json()

def send_request(
    request_type: str, 
    url_path: str, 
    params: Optional[dict] = None,
    body: Optional[dict] = None
):
    try:
        if request_type == 'GET':
            response = requests.get(url_path)
        elif request_type == 'POST':
            response = requests.post(url_path)
        else:
            raise Exception(f"{request_type} not supported")
        
        if not response.ok:
            try:
                error_data = response.json()
                return {"error": f"Request failed with status {response.status_code}", "details": error_data}
            except:
                return {"error": f"Request failed with status {response.status_code}", "text": response.text[:500]}
            
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return {"message": "Success (No JSON returned)", "text": response.text[:500]}
            
    except Exception as e:
        return {"error": str(e)}
    
def main(task_name):
    print(f"Sending request for task: {task_name}")
    result = send_request(request_type="POST", url_path=f"http://127.0.0.1:8000/run/{task_name}")
    print(result)

if __name__ == "__main__":
    task = sys.argv[1] if len(sys.argv) > 1 else "task_Hello_world"
    main(task)