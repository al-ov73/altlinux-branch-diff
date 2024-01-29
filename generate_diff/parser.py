import requests
import pandas as pd
from pandas import DataFrame



api_url = 'https://rdb.altlinux.org/api/'
export_url = 'export/branch_binary_packages/'
# p10_url = ''
# sisyphus = ''



def parse_url(url):
    return requests.get(url)

p10_url = api_url + export_url + 'p10'
sisyphus_url = api_url + export_url + 'sisyphus'

p10_response = parse_url(p10_url).json()
sisyphus_response = parse_url(sisyphus_url).json()

p10_packages_list = (p10_response['packages'])

# print(len(p10_packages_list), type(p10_packages_list))
# p10_packages_dict = {package['name']: package for package in p10_packages_list}
# print(len(p10_packages_dict))
sisyphus_packages_list = (sisyphus_response['packages'])
# print(len(sisyphus_packages_list), type(sisyphus_packages_list))
# sisyphus_packages_dict = {package['name']: package for package in sisyphus_packages_list}
# print(len(sisyphus_packages_dict))


df1 = pd.DataFrame(p10_packages_list)
df2 = pd.DataFrame(sisyphus_packages_list)

diff = pd.concat([df1, df2]).drop_duplicates(keep=False)

print(diff.to_dict)

# comparison = df1.merge(df2, indicator=True, how='outer')
# diff = comparison[comparison['_merge'] != 'both']
# print(len(diff))
# print(diff)