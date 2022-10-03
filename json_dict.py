import requests

url = "https://impactcloud.sopact.com/api.php/high-chart/336/get_outcome_insights_data/451fb330d42a42021fe502c5a0015614?default_language=en"

payload = "{\n  \"data\": {\n    \"type\":\"N\",\n    \n    \"metric_set_ids\": [\n      2613\n    ],\n    \n    \"project_ids\": [\n      1423\n    ]\n  }\n}"
headers = {
  'Content-Type': 'text/plain',
  'Cookie': 'AWSALB=ujZCs1r+dppw169ruUYfxnd2B5BwbQrd/qppRbL+eMV7M6DDgX+vsqTOGwkzHkEl/efJjhREOCU9A1Ht+AiZjDT/pnVXdywAWk7YSIuaO1pHlIJn+L866WG//NnX; AWSALBCORS=ujZCs1r+dppw169ruUYfxnd2B5BwbQrd/qppRbL+eMV7M6DDgX+vsqTOGwkzHkEl/efJjhREOCU9A1Ht+AiZjDT/pnVXdywAWk7YSIuaO1pHlIJn+L866WG//NnX; PHPSESSID=srgmeu7jebo4jfnrcol9c114r0'
}

response = requests.request("POST", url, headers=headers, data=payload)
results = response.json()



if results['message'] == 'Data found.':
    columns = results['data']['datatype']
    # print("🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀 ~ file: json_dict.py ~ line 18 ~ columns", columns)
    column_values = columns.keys()
    print("________________________________________",results['data']['contents'])