network = {
    "sites": [
        {
            "name": "Sydney",
            "devices": [
                {
                    "hostname": "R1",
                    "interfaces": [
                        {"name": "Gig0/1", "status": "up",   "in_bytes": 12345, "errors": 0},
                        {"name": "Gig0/2", "status": "down", "in_bytes":     0, "errors": 2},
                    ],
                },
                {
                    "hostname": "R2",
                    "interfaces": [
                        {"name": "Gig0/3", "status": "up", "in_bytes": 500, "errors": 1},
                    ],
                },
            ],
        },
        {
            "name": "Melbourne",
            "devices": [
                {
                    "hostname": "R3",
                    "interfaces": [
                        {"name": "Eth0", "status": "up", "in_bytes": 800, "errors": 0},
                        {"name": "Eth1", "status": "down", "in_bytes": 10, "errors": 5},
                    ],
                },
            ],
        },
    ]
}


summary = {}

temp = []

for sites in network["sites"]:
    temp = []
    # print(sites["name"]
    for city in sites["devices"]:
        # print(city["hostname"])
        if sites["name"] not in summary:
            temp.append(city["hostname"])
    if sites["name"] not in summary:
        summary[sites["name"]] = temp
        

print(summary)
