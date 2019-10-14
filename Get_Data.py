import Constant
import Config_Post_Data


def get_shipment_report(session_requests, csrf, oid):
    # SEND FIRST POST REQUEST
    data_dict = Config_Post_Data.config_shipment_report_by_oid(csrf, oid)

    response = session_requests.post(
        Constant.url_list_shipments,
        data=data_dict
    )

    # SEND FOLLOWING GET REQUESTS

    get_urls = Constant.re_pattern_url_parse.findall(response.text)
    for url in get_urls:
        session_requests.get(Constant.url_tms_root + url)

    # SEND SECOND POST REQUEST
    data_dict['norefresh'] = ''
    data_dict['nSetNumber'] = 1

    response = session_requests.post(
        Constant.url_list_shipments,
        data=data_dict
    )

    return response


def parse_data(html_script, re_pattern):

    data_dict = dict()
    data_list = re_pattern.findall(html_script)

    for col_name in Constant.list_col_name:
        data_dict[col_name] = list()
    for values in data_list:
        for i, value in enumerate(values):
            value = value.replace(Constant.html_equivalence_and, '&')
            data_dict[Constant.list_col_name[i]].append(value)

    return data_dict


def read_login_credentials():
    login_userid = open('username.txt', mode='r')
    login_password = open('password.txt', mode='r')

    Constant.login_userid = login_userid.read()
    Constant.login_password = login_password.read()

    print('User credentials read successfully.')
