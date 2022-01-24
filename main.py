import math
from tkinter import E
from wsgiref import headers
from xml.dom import ValidationErr
from xmlrpc.client import ResponseError
from data_structures.datacenter import Datacenter
from data_structures.network_collection import NetworkCollection
from data_structures.entry import Entry
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import time, requests


# http.client.HTTPConnection.debuglevel = 1

URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"


def get_data(url, max_retries=5, delay_between_retries=1):
    """
    Fetch the data from http://www.mocky.io/v2/5e539b332e00007c002dacbe
    and return it as a JSON object.

    Args:
        url (str): The url to be fetched.
        max_retries (int): Number of retries.
        delay_between_retries (int): Delay between retries in seconds.
    Returns:
        data (dict)
    """

    current_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    counter = 0
    on_succes = False
    while counter < max_retries and not on_succes:
        try:
            response = requests.get(url, timeout=5, headers=current_headers)
            on_succes = True
        except Exception as e:
            print("Connection error! Waiting %s sec and re-trying" % delay_between_retries)
            time.sleep(delay_between_retries)
            counter += 1
            print(counter)
            if counter == 5:
                break
    if on_succes:
        try:
            return response.json()
        except (ValueError, ValidationErr):
            return None


def deep_copy(data, datacenter, keyword):
    network_data = {}

    for elem in datacenter:
        for value in elem.cluster_dict:
            for key in list(data[elem.name][value][keyword].keys()):
                network_data[key] = data[elem.name][value][keyword][key]

    return network_data


def main():

    data = get_data(URL)

    if not data:
        raise ValueError('No data to process')

    datacenters = [Datacenter(key, value) for key, value in data.items()]

    for elem in datacenters:
        elem.remove_invalid_clusters()

    network_data = deep_copy(data, datacenters, 'networks')

    nw_collection = ([NetworkCollection(key, value) for key, value in network_data.items()])

    for elem in nw_collection:
        elem.remove_invalid_records()

    for elem in nw_collection:
        #setattr(self, elem.entries['address'], lambda d: d['address'] )
        #print(elem.ipv4_network)
        #print(sorted(elem.entries))
        #print((elem.ipv4_network))
        print(sorted(elem.entries, key=lambda d: d['address']))


if __name__ == '__main__':
    main()
