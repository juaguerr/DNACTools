from rest_connection import dnac
import pandas as pd
import xlwt

'''Takes in a number n, returns the square of n'''

def list_devices():
    '''List devices on Console in a Data Frame Format'''
    url = '/dna/intent/api/v1/network-device'
    devices = dnac.get_request(url)
    df = pd.DataFrame(columns=["Hostname", "Family", "Model", "Role", "Mgmt IP", "Location", "Version", "Reacheability","UpTime","Serial"])
    for i in devices['response']:
        df = df.append({"Hostname":i['hostname'],"Family":i['family'],
                        "Model":i['platformId'], "Role":i['role'], 
                        "Mgmt IP":i['managementIpAddress'], "Location":i['location'],"Version":i['softwareVersion'], 
                        "Reacheability":i['reachabilityStatus'],"UpTime":i['upTime'],"Serial":i['serialNumber'] }, ignore_index=True)
    print(df)
    return None

def list_devices_to(argv):
    '''Create a XLS and CSV file with the Device List
    :param argv: defines the output, should be xls or csv
    '''
    url = '/dna/intent/api/v1/network-device'
    devices = dnac.get_request(url)
    df = pd.DataFrame(columns=["Hostname", "Family", "Model", "Role", "Mgmt IP", "Location", "Version", "Reacheability","UpTime","Serial"])
    for i in devices['response']:
        df = df.append({"Hostname":i['hostname'],"Family":i['family'],
                        "Model":i['platformId'], "Role":i['role'], 
                        "Mgmt IP":i['managementIpAddress'], "Location":i['location'],"Version":i['softwareVersion'], 
                        "Reacheability":i['reachabilityStatus'],"UpTime":i['upTime'],"Serial":i['serialNumber'] }, ignore_index=True)
    if argv == 'csv':
        df.to_csv('device_list.csv')
    elif argv == 'xls':
        df.to_excel('device_list.xls')
    return None


def client_health():  
    '''Overall Clieth Health'''
    url = '/dna/intent/api/v1/client-health'
    clients = dnac.get_request(url)
    return clients['response']
