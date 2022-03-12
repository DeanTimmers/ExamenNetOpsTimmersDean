url = "https://api.domainsdb.info/v1/domains/search?domain=syntra.be"

import requests as api_url
import yaml
import re

response = api_url.get(f"{url}")
response_data = response.json()

created = r"(?P<jaar>\d{4})-(?P<maand>\d{2})-(?P<dag>\d{2})"
provider = r"\.(?P<provider>\w+)\."

output = {
    "created":
        {
        "dag": "",
        "jaar": "",
        "maand": ""
        },
    "ip": "",
    "land": "",
    "provider": ""
        }

output["land"] = response_data["domains"][0]["country"]
output["ip"] = response_data["domains"][0]["A"][0]
output["provider"] = re.findall(provider,response_data["domains"][0]["NS"][0])[0]

for match in re.finditer(created, response_data["domains"][0]["create_date"]):
    output["created"] = match.groupdict()

print(yaml.dump(output))

