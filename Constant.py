from re import compile
from pandas import read_excel

root_path = 'C:\\Users\\Zhou_Charles\\Desktop\\'
file_name_bg_trade_rule_depository = 'B&G_Trade_Rule_Depository.xlsx'

time_format_military = '%m/%d/%Y %H:%M'
process_name = 'B&G Trade Update'
g_sheets_workbook_id_log = '1Yudm7JfKSgL82zyHXnDKUjJfoI5VGoEsPHgysPXcZ4g'
g_sheets_worksheet_id_log = 0

login_userid = None
login_password = None

url_tms_login = 'https://dsclogistics.mercurygate.net/MercuryGate/login/LoginProcess.jsp'
url_list_transports = 'https://dsclogistics.mercurygate.net/MercuryGate/transport/listTransports.jsp'
url_list_shipments = 'https://dsclogistics.mercurygate.net/MercuryGate/shipment/listShipment.jsp'
url_tms_root = 'https://dsclogistics.mercurygate.net'


url_get_request_ref_type_initial = 'https://dsclogistics.mercurygate.net/MercuryGate/common/extClassLoader.jsp?appName=' \
                                  'MG.tms.portlet.enterprise.ReferenceTypesApp'
url_post_request_ref_type = 'https://dsclogistics.mercurygate.net/MercuryGate/extJsPortletData/ReferenceTypesPortlet'

url_post_add_ref = 'https://dsclogistics.mercurygate.net/MercuryGate/common/addReference_process.jsp'


re_pattern_csrf = compile('\<meta name\=\"_csrf\" content\=\"([\w\-]*)\" \/\>')
re_pattern_url_parse = compile('\<script src\=\"([\w\/\.\?\=]*)\" type\=\"text\/javascript\"\>\<\/script\>')

list_col_name = [
    'menu_value',
    'oid',
    'load_ref',
    'owner',
    'shipment_type',
    'origin_code',
    'dest_code',
    'trade_flag',
    'carrier_mode',
    'actual_ship'
]

re_pattern_all_cols = compile('sMenuValue\=(\(\d{11}\,\d{4}\,\d{1}\)).*?\<\/td\>\s*'
                                 '\<td align\=.+?\>(\d{11})\<\/td\>\s*'
                                 '\<td align\=.+?\>(.*?) \(.+?\<\/td\>\s*'
                                 '\<td align\=.+?\>(.*?)\<\/td\>\s*'
                                 '\<td align\=.+?\>(.*?)\<\/td\>\s*'
                                 '\<td align\=.+?\>(.*?)\<\/td\>\s*'
                                 '\<td align\=.+?\>(.*?)\<\/td\>\s*'
                                 '\<td align\=.+?\>(.*?)\<\/td\>\s*'
                                 '\<td align\=.+?\>(.*?)\<\/td\>\s*'
                                 '\<td align\=.+?\>(.*?)\<\/td\>')

field_origin_code = 'OriginLocation.LocationCode'
field_create_date = 'CreateDate'
field_type = 'Type'
field_origin_state = 'OriginLocation.State'
field_origin_city = 'OriginLocation.City'
field_origin_name = 'OriginLocation.Name'
field_oid = 'Oid'
field_location_code = 'LocationCode'
field_name = 'Name'
field_city = 'City'
field_state = 'State'
field_address1 = 'Address1'
field_address2 = 'Address2'
field_postal_code = 'PostalCode'
field_country = 'Country'
field_status = 'Status'
field_agent_number = 'Ref: 16697125400'
field_batch = 'Ref: 53580617477'
field_bid_board = 'Ref: 54674644540'
field_bol = 'Ref: 1200'
field_customer_code = 'Ref: 61133800'
field_customer_ref_number = 'Ref: 4427918800'
field_del_appt = 'Ref: 4750584900'
field_del_late_party = 'Ref: 51370999000'
field_del_late_reason= 'Ref: 42601492700'
field_dsc_special_services = 'Ref: 40532775900'
field_first_tender = 'Ref: 54451972337'
field_item_not_matched = 'Ref: 16743044800'
field_load_number = 'Ref: 1174978200'
field_dest_not_matched = 'Ref: 17085562600'
field_origin_not_matched = 'Ref: 16743044900'
field_shipment_type = 'Ref: 4492548900'
field_tri = 'Ref: 54192117830'
field_trade= 'Ref: 19217908000'
field_subtrade = 'Ref: 54144713184'
field_assigned_to = 'AssignedTo'
field_carrier_scac = 'FirstSelectedChargeSheet.CarrierSCAC'

filter_equal = 'Equal'
filter_in = 'In'
filter_not_in = 'Not In'
filter_not_equal = 'Not Equal'
filter_from_today = 'From Today'
filter_begins_with = 'Begins With'
filter_not_begins_with = 'Not Begin With'

# oid_enterprise = 16682284300 #Legacy
oid_enterprise = 54775198209 #ezVision
oid_trade_flag_report = None
oid_subtrade_flag_report = None

menu_value_ref_type_trade = '(19217908000,3250,0)'

html_equivalence_and = '&amp;'

post_data_open_report = {
    '_csrf': '',
    'SelectedObjs': '',
    'PageChange': 'false',
    'sidAction': '',
    'action': '',
    'fromExt': 'false',
    'reportoid': ''
}


post_data_add_ref = {
    '_csrf': '',
    'sidOwner': '',
    'nNumberOfReferences': '1',
    'sReturnURL': '',
    'SelectedObjs': '',
    'listOids': '',
    'typeOwner': '3700',
    'isFromListScreen': 'false',
    'ListCacheKey': '',
    'sidReferenceType1': '',
    'refType1': 'value',
    'sSequence1': '',
    'SR192179080001': None,
    'sContactField1': 'name'
}

trade_c_origin_code_in = read_excel(file_name_bg_trade_rule_depository, sheet_name='C')['ORIGIN_CODE_IN'].tolist()
trade_f_origin_code_in = read_excel(file_name_bg_trade_rule_depository, sheet_name='F')['ORIGIN_CODE_IN'].tolist()
trade_i_origin_code_in = read_excel(file_name_bg_trade_rule_depository, sheet_name='I')['ORIGIN_CODE_IN'].tolist()
trade_n_origin_code_in = read_excel(file_name_bg_trade_rule_depository, sheet_name='N')['ORIGIN_CODE_IN'].tolist()
trade_o_origin_code_in = read_excel(file_name_bg_trade_rule_depository, sheet_name='O')['ORIGIN_CODE_IN'].tolist()
trade_t_origin_code_in = read_excel(file_name_bg_trade_rule_depository, sheet_name='T')['ORIGIN_CODE_IN'].tolist()
trade_zc_origin_code_in = read_excel(file_name_bg_trade_rule_depository, sheet_name='ZC')['ORIGIN_CODE_IN'].tolist()
trade_zf_origin_code_in = read_excel(file_name_bg_trade_rule_depository, sheet_name='ZF')['ORIGIN_CODE_IN'].tolist()
trade_zi_origin_code_in = read_excel(file_name_bg_trade_rule_depository, sheet_name='ZI')['ORIGIN_CODE_IN'].tolist()
trade_zo_origin_code_in = read_excel(file_name_bg_trade_rule_depository, sheet_name='ZO')['ORIGIN_CODE_IN'].tolist()

trade_c_dest_code_not_in = read_excel(file_name_bg_trade_rule_depository, sheet_name='C')['DEST_CODE_NOT_IN'].tolist()
trade_f_dest_code_in = read_excel(file_name_bg_trade_rule_depository, sheet_name='F')['DEST_CODE_IN'].tolist()
trade_i_dest_code_in = read_excel(file_name_bg_trade_rule_depository, sheet_name='I')['DEST_CODE_IN'].tolist()
trade_n_dest_code_in = read_excel(file_name_bg_trade_rule_depository, sheet_name='N')['DEST_CODE_IN'].tolist()
trade_o_dest_code_in = read_excel(file_name_bg_trade_rule_depository, sheet_name='O')['DEST_CODE_IN'].tolist()
trade_t_dest_code_not_in = read_excel(file_name_bg_trade_rule_depository, sheet_name='T')['DEST_CODE_NOT_IN'].tolist()
trade_zc_dest_code_not_in = read_excel(file_name_bg_trade_rule_depository, sheet_name='ZC')['DEST_CODE_NOT_IN'].tolist()
trade_zf_dest_code_in = read_excel(file_name_bg_trade_rule_depository, sheet_name='ZF')['DEST_CODE_IN'].tolist()
trade_zi_dest_code_in = read_excel(file_name_bg_trade_rule_depository, sheet_name='ZI')['DEST_CODE_IN'].tolist()
trade_zo_dest_code_in = read_excel(file_name_bg_trade_rule_depository, sheet_name='ZO')['DEST_CODE_IN'].tolist()

print('B&G trade rule depository loaded successfully.')