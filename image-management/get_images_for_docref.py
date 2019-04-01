import furl
import pprint
import requests
from pymongo import MongoClient


def get_iaid_from_reference(docref):
    s = requests.Session()

    collection_query_url: furl.furl = collection_endpoint_url / docref

    r: requests.Response = s.get(url=collection_query_url)
    # print(r.status_code)
    r.raise_for_status()
    # might also want to setup headers properly (as constants?), set timeouts etc

    return r.json()["assets"][0]["id"]

client = MongoClient()

API_BASE_URL: furl.furl = furl.furl(r"http://discovery.nationalarchives.gov.uk/API/")
API_VERSION = "v1/"
#more constants such as translating numeric catalogue levels into lettercode, division, series... ?

RECORDS_PATH_FRAGMENT = "records/"
COLLECTION_PATH_FRAGMENT = "collection/"
CHILDREN_PATH_FRAGMENT = "children/"

#would probably move API groups into their own modules, with classes for each endpoint?
records_api = API_BASE_URL / RECORDS_PATH_FRAGMENT / API_VERSION
collection_endpoint_url: furl.furl = records_api / COLLECTION_PATH_FRAGMENT

citable_ref: str = "WO 95/1104"
iaid = get_iaid_from_reference(citable_ref)
print(iaid)

isParent = r.json()["assets"][0]["isParent"]
#would probably want to check eg catalogueLevel, length of assets list, and isParent too
assert isinstance(iaid, str)
print(iaid,isParent)

#should make this a function to be called recursively as we work down hierarchy, needs to work through assets list
#at each level too.
if isParent:
    children_endpoint_url: furl.furl = records_api / CHILDREN_PATH_FRAGMENT
    children_query_url: furl.furl = children_endpoint_url / iaid

    assert isinstance(children_query_url, furl.furl)
    r2 = s.get(url=children_query_url)
    pprint.pprint(r2.json())


