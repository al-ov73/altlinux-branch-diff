import json
import os

import requests
from pathlib import Path


api_url = 'https://rdb.altlinux.org/api/'
export_url = 'export/branch_binary_packages/'

p10_url = api_url + export_url + 'p10'
sisyphus_url = api_url + export_url + 'sisyphus'


def parse_url():
    print('Collectind data...')
    p10_response = requests.get(p10_url).json()
    sisyphus_response = requests.get(sisyphus_url).json()

    p10_packages_list = (p10_response['packages'])

    print("Current arch's")
    print(set(a['arch'] for a in p10_packages_list))
    arch = input('Choose arch you want to check: ')
    sisyphus_pack_list = (sisyphus_response['packages'])

    p10_arch_list = [package for package in p10_packages_list if
                     package["arch"] == arch]
    sisyphus_arch_list = [
        package for package in sisyphus_pack_list if package["arch"] == arch
    ]
    p10_dict = {package['name']: package for package in p10_packages_list}
    sisyphus_dict = {package['name']: package for package in sisyphus_pack_list}
    total = len(sisyphus_pack_list + sisyphus_arch_list)
    print('Total packages both in p10 and sisyphus:')
    print(total)
    answer = input(
        "Choose type of connection"
        "('p10', 'sisyphus', 'both', 'sisyphus-newer'): ")
    match answer:
        case 'p10':
            result = [package for package in p10_arch_list if p10_dict[
                package['name']] != sisyphus_dict.get(
                package.get('name'))]
        case 'sisyphus':
            result = [pack for pack in sisyphus_arch_list if
                      sisyphus_dict[pack['name']] != p10_dict.get(
                          pack.get('name'))]
        case 'both':
            result = [package for package in p10_arch_list if p10_dict[
                package['name']] == sisyphus_dict.get(
                package.get('name'))]

        case 'sisyphus-newer':
            p10_dict = {package['name']: package for package in p10_arch_list}
            result = [package for package in sisyphus_arch_list if (
                        (package['name'] in p10_dict.keys()) and (
                            package['version'] >
                            p10_dict[package['name']]['version']))]

        case _:
            print('not supported option :(')
            return
    with open('data.json', 'w') as f:
        json.dump(result, f, indent=4)
    BASE_DIR = Path(__file__).resolve().parent.parent
    print('You can find result.json using link below:')
    result_url = os.path.join(BASE_DIR, 'data.json')
    print(result_url)


# ВАРИАНТ С ИСПОЛЬЗОВАНИЕМ PANDAS
# def parse_url():
#     print('Collectind data...')
#     p10_response = requests.get(p10_url).json()
#     sisyphus_response = requests.get(sisyphus_url).json()
#
#     p10_packages_list = (p10_response['packages'])
#
#     print("Current arch's")
#     print(set(a['arch'] for a in p10_packages_list))
#     arch = input('Choose arch you want to check: ')
#     sisyphus_pack_list = (sisyphus_response['packages'])
#
#     p10_arch_list = [package for package in p10_packages_list if
#                      package["arch"] == arch]
#     sisyphus_arch_list = [
#         p for p in sisyphus_pack_list if p["arch"] == arch
#     ]
#
#     df1 = pd.DataFrame(p10_arch_list)
#     df2 = pd.DataFrame(sisyphus_arch_list)
#     df1.to_json('p10_packages.json', orient='records',
#                               lines=True)
#     df2.to_json('sisyphus_packages.json',
#                                    orient='records',
#                                    lines=True)
#     df = pd.merge(df1, df2, how='outer', indicator=True)
#
#     total = df.shape[0]
#     print('Total packages both in p10 and sisyphus:')
#     print(total)
#     answer = input("Choose type of connection ('p10', 'sisyphus', 'both'): ")
#     match answer:
#         case 'p10':
#             result = df.loc[(df._merge == 'left_only')]
#         case 'sisyphus':
#             result = df.loc[(df._merge == 'right_only')]
#         case 'both':
#             result2 = df.loc[(df._merge == 'both')]
#         case _:
#             print('not supported option :(')
#             return
#
#     print(result.shape[0])
#     result.to_json('result.json', orient='records', lines=True)
#     BASE_DIR = Path(__file__).resolve().parent.parent
#     print('You can find result.json using link below:')
#     result_url = os.path.join(BASE_DIR, 'result.json')
#     print(result_url)
