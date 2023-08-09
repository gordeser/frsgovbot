import requests

cookies = {
    'SESSION': '',
}

json_data = {
    'from': '2023-08-10',
    'to': '2023-12-31',
    'accompanyingPersons': 0,
    'agenda': {
        'id': '15245207-2ff7-4f8a-8aa3-34273c46bb8c',
    },
}

response = requests.post(
    'https://frs.gov.cz/api/ip/external/timetable/slots',
    cookies=cookies,
    json=json_data,
)

ans = response.json()

for slot in ans:

    times = ans[slot]
    if len(times) != 0:
        for time in times:
            capacity = times[time]['capacity']
            occupied = times[time]['occupied']
            if capacity != occupied:
                print("ALERT", time, slot, capacity, occupied)
