import pdb 
from models.task import Task
import repos.task_repo as task_repository  

result = task_repository.select_all()

for task in result:
    print(task.__dict__)

pdb.set_trace()