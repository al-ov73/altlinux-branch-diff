import requests
import pandas as pd


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
    sisyphus_packages_list = (sisyphus_response['packages'])

    p10_arch_list = [package for package in p10_packages_list if
                     package["arch"] == arch]
    sisyphus_arch_list = [
        package for package in sisyphus_packages_list if package["arch"] == arch
    ]

    df1 = pd.DataFrame(p10_arch_list)
    df2 = pd.DataFrame(sisyphus_arch_list)

    df = pd.merge(df1, df2, how='outer', indicator=True)

    total = df.shape[0]
    print('Total packages both in p10 and sisyphus:')
    print(total)
    answer = input('Choose type of connection (p10, sisyphus, both): ')
    match answer:
        case 'p10':
            option = 'left_only'
        case 'sisyphus':
            option = 'right_only'
        case 'both':
            option = 'both'
        case _:
            print('not supported option :(')
            return
    result = df.loc[df._merge == option].shape[0]
    print(result)