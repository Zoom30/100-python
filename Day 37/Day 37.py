import requests
from datetime import datetime
import api_keys

pixela_endpoint = "https://pixe.la/v1/users"





graph_endpoint = f"{pixela_endpoint}/{api_keys.user_params['username']}/graphs"

graph_params = {
    "id": "graph15",
    "name": "Programming Hours Graph",
    "unit": "Hours",
    "type": "int",
    "color": "ichou"
}
headers = {
    "X-USER-TOKEN": api_keys.user_params["token"]
}

# graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(graph_response.text)


#posting value to graph

optional_data = {
    "number of hours max": 6,
    "average": 3,
    "ideal": 4
}

date = datetime(year=2021, month=7, day=18)

value_graph_params = {
    "date": date.strftime("%Y%m%d"),
    "quantity": "9"
}

# value_response = requests.post(url=f"{pixela_endpoint}/dani/graphs/{graph_params['id']}", json=value_graph_params, headers=headers)
# print(value_response.text)

update_graphs_params = {
    "quantity": "2"
}

# update_graphs_response = requests.put(url=f"{pixela_endpoint}/{user_params['username']}/graphs/{graph_params['id']}/{date.strftime('%Y%m%d')}", json=update_graphs_params, headers=headers)
# print(update_graphs_response.text)

delete_response = requests.delete(url=f"{pixela_endpoint}/{api_keys.user_params['username']}/graphs/{graph_params['id']}/{date.strftime('%Y%m%d')}", headers=headers)
print(delete_response.text)