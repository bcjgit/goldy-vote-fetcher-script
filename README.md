# Noun vote image downloader script
by: brianj (@pbrianandj)

## How to run

1. `pip install -r requirements.txt`
2. `python fetch_votes.py YOUR_PROP_NUMBER_HERE`

It will create a folder in the direct your run it in called `prop-{YOUR PROP NUMNER}`.
In this folder, there will be two other folders: yes and no.

Within each of these folders will be 1 svg per Noun voting yes or no. Abstensions are not processed.

