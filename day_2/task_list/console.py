import pdb
from models.task import Task
from models.user import User

import repos.task_repo as task_repo
import repos.user_repo as user_repo

task_repo.delete_all()
user_repo.delete_all()

user1 = User("Jack", "Jarvis")
user_repo.save(user1)
user2 = User("Victor", "McDade")
user_repo.save(user2)

user_repo.select_all()

task_1 = Task("Plant seeds", user1, 30)
task_repo.save(task_1)

task_2 = Task("Go for a run", user1, 30, True)
task_repo.save(task_2)


# pdb.set_trace()
