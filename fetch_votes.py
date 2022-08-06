import sys
from python_graphql_client import GraphqlClient
import requests
import os
from tqdm import tqdm

PROP_ID = int(sys.arvg[1])

# Instantiate the client with an endpoint.
client = GraphqlClient(endpoint="https://api.thegraph.com/subgraphs/name/nounsdao/nouns-subgraph")

query = """
{
  proposal(id: "%s") {
    votes {
      supportDetailed
      nouns {
        id
        seed
        {
            background
            body
            accessory
            head
            glasses
        }
      }
    }
  }
}
""" % (PROP_ID)
# Synchronous request
data = client.execute(query=query)

yes_nouns = []
no_nouns = []

for vote in data['data']['proposal']['votes']:
    if vote['supportDetailed'] == 1:
        yes_nouns.extend(vote['nouns'])
    if vote['supportDetailed'] == 0:
        no_nouns.extend(vote['nouns'])


filename = f"./prop-{PROP_ID}"
os.makedirs(os.path.dirname(filename), exist_ok=True)

filename = f"./prop-{PROP_ID}/yes"
os.makedirs(filename, exist_ok=True)


filename = f"./prop-{PROP_ID}/no"
os.makedirs(filename, exist_ok=True)


for noun in tqdm(yes_nouns):
    seed = noun['seed']
    response = requests.get('https://api.cloudnouns.com/v1/pfp?seed={background},{body},{accessory},{head},{glasses}'.format(
        background=seed['background'],
        body=seed['body'],
        accessory=seed['accessory'],
        head=seed['head'],
        glasses=seed['glasses']
    ))
    nounId = noun['id']

    filename = f'./prop-{PROP_ID}/yes/noun-{nounId}.svg'
    with open(filename, 'w') as f:
        f.write(response.text)

for noun in tqdm(no_nouns):
    seed = noun['seed']
    response = requests.get('https://api.cloudnouns.com/v1/pfp?seed={background},{body},{accessory},{head},{glasses}'.format(
        background=seed['background'],
        body=seed['body'],
        accessory=seed['accessory'],
        head=seed['head'],
        glasses=seed['glasses']
    ))
    nounId = noun['id']

    filename = f'./prop-{PROP_ID}/no/noun-{nounId}.svg'
    with open(filename, 'w') as f:
        f.write(response.text)

print("Done! Stay Nounish ⌐◨-◨")
