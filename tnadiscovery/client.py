import requests
# import datetime
# import xml.etree.ElementTree as ET
import furl

#from .resource import Bill, EDM, Division, Member, parse_data, MemberList
#from .parties import Parties


class Discovery():
    API_BASE_URL = furl.furl(r"http://discovery.nationalarchives.gov.uk/API/")
    API_VERSION = "v1/"
    RECORDS_PATH_FRAGMENT = "records/"
    COLLECTION_PATH_FRAGMENT = "collection/"
    CHILDREN_PATH_FRAGMENT = "children/"
    SEARCH_PATH_FRAGMENT = "search/"

    records_api = API_BASE_URL / RECORDS_PATH_FRAGMENT / API_VERSION
    search_api  = API_BASE_URL / SEARCH_PATH_FRAGMENT / API_VERSION

    def __init__(self):
        self.http = requests.Session()

    def get_ia(self, iaid):
        # res = self.get(Discovery.records_api.add("details/",iaid))
        Discovery.records_api.path.add("details/"+iaid)
        data = self.get(Discovery.records_api)
        ia = InformationAsset(data)
        return ia

    def search(self,term):
        params = {"sps.searchQuery": term}
        Discovery.search_api.path.add("records")
        r = requests.get(Discovery.search_api, params=params)
        data = r.json()
        return data

    def get(self, url):
        res = self.http.get(url)
        res.raise_for_status()
        data = res.json()
        return data


class InformationAsset(object):
    def __init__(self,data):
        self.data = data

    def get_iaid(self):
        return self.data['id']

    def get_description(self):
        return self.data['scopeContent']['description']
