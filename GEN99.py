import csv
import requests
import list_filter
from datetime import date

# Function to get JSON data
def get_json(api, auth):
    try:
        response = requests.get(api, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print "Error occurred: %s" % err
        return None


BR = ['BR0_PROJ4','BR1_PROJ0','BR1_PROJ2','BR3_PROJ1']
IT = ['HOST','TARGET']

job_to_csv_map = {
    'GEN99_BR0_PROJ4_LKG_HOST_JSP_IT': ['BR0', 'LIBER(HOST_JSP_IT)'],
    'GEN99_BR0_PROJ4_LKG_TARGET_JSP_IT': ['BR0', 'LIBER(TARGET_JSP_IT)'],
    'GEN99_BR1_PROJ0_LKG_HOST_JSP_IT': ['BR1', 'MT6835(HOST_JSP_IT)'],
    'GEN99_BR1_PROJ0_LKG_TARGET_JSP_IT': ['BR1', 'MT6835(TARGET_JSP_IT)'],
    'GEN99_BR1_PROJ2_LKG_HOST_JSP_IT': ['BR1', 'MT6897(HOST_JSP_IT)'],
    'GEN99_BR1_PROJ2_LKG_TARGET_JSP_IT': ['BR1', 'MT6897(TARGET_JSP_IT)'],
    'GEN99_BR3_PROJ1_LKG_HOST_JSP_IT': ['BR3', 'CHIP11207(HOST_JSP_IT)'],
    'GEN99_BR3_PROJ1_LKG_TARGET_JSP_IT': ['BR3', 'CHIP11207(TARGET_JSP_IT)'],
}

url = "http://10.21.35.9:8080"
auth = ('123456', '654312')

write_data=[]
fail=[]

for proj in BR:
    for host in IT:
        job_name = 'GEN99_{}_LKG_{}_JSP_IT'.format(proj,host)
        file_name = 'working/common.ews_{}_jsp_it/perf_report.csv'.format(host.lower())
        
        cl_api = "{}/job/{}/lastCompleteBuild/api/json".format(url, job_name)
        file_api = "{}/job/{}/lastCompleteBuild/artifact/{}".format(url, job_name, file_name)
        
        job_data = get_json(cl_api, auth)
        if not job_data:
            fail.append([job_name, file_name])
            continue

        response = requests.get(file_api, auth=auth)
        if response.status_code == 200:
            decoded_content = response.content.decode('utf-8')
            csv_reader = csv.reader(decoded_content.splitlines(),delimiter=',')
            data_list = list(csv_reader)

            cash = [
                [int(item) if item.isdigit() else item for item in sublist]
                for sublist in data_list if 'NA' not in sublist
            ]

            cash = list_filter.list_semsller_int(cash,100,3)
            for item in cash:
                write_data.append(job_to_csv_map[job_name] + item[1:3] + [date.today().strftime("%m/%d/%Y"), str(job_data['actions'][0]['parameters'][7]['value']), str(job_data['number'])])
        else:
            fail.append([job_name, file_name])


with open('GEN.csv','wb') as out_file:
    writer = csv.writer(out_file)
    for item in write_data:
        writer.writerow(item)

with open('FAID.csv','wb') as out_file:
    writer = csv.writer(out_file)
    for item in fail:
        writer.writerow(item)
