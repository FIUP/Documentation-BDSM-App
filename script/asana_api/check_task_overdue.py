from newapi import my_api
from date import date

# MAIN

# see your workspaces
my_api_asana = my_api.MyAPI()
my_date = date.Date()

id_proj_str = my_api_asana.get_id_workspace("mashup-unipd.it")
# id del progetto: Fasi di Avanzamento
tasks_project = my_api_asana.get_asana_api().get_project_tasks(21682627966289)

for task in tasks_project:

    if my_api_asana.get_asana_api().get_task(task['id'])['completed_at'] is not None:

        date_task_complete_str = (my_api_asana.get_asana_api().get_task(task['id'])['completed_at'])[0:10]
        date_task_due_str = (my_api_asana.get_asana_api().get_task(task['id'])['due_on'])[0:10]
        date_complete_dt = date.Date.convert_date(date_task_complete_str)
        date_due_task_dt = date.Date.convert_date(date_task_due_str)
        print date_due_task_dt