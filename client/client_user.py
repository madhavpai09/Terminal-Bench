import requests
from typing import Optional

def taskset_create_request(taskset_name:str):
    url = f"http://127.0.0.1:8000/tasksets/create/{taskset_name}"
    response = requests.post(url)
    return response.json()

def taskset_run_request(taskset_name:str):
    url  = f"http://127.0.0.1:8000/tasksets/run/{taskset_name}"
    response = requests.post(url)
    return response.json()
                 
def task_run_request(task_name:str):
    url = f"http://127.0.0.1:8000/tasks/run/{task_name}"
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
            return {"message": "Success", "text": response.text[:500]}
            
    except Exception as e:
        return {"error": str(e)}
    


        
    