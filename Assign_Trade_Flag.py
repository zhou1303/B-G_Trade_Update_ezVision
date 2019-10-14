import Constant


def is_trade_ac(origin_code, shipment_type):
    if '1010' in origin_code \
            and ('CPU' in shipment_type.upper() or 'CUSTOMER ROUTED' in shipment_type.upper()):
        return True
    return False


def is_trade_ap(origin_code, carrier_mode, ):
    if '1010' in origin_code and 'PAR' in carrier_mode.upper():
        return True
    return False


def is_trade_c(origin_code, dest_code, shipment_type):
    if origin_code in Constant.trade_c_origin_code_in and dest_code not in Constant.trade_c_dest_code_not_in \
            and 'DISPOSAL' not in shipment_type.upper() \
            and 'CPU' not in shipment_type.upper():
        return True
    return False


def is_trade_d(carrier_mode):
    if 'DRAY' in carrier_mode.upper():
        return True
    return False


def is_trade_f(origin_code, dest_code):
    if origin_code in Constant.trade_f_origin_code_in \
            and dest_code in Constant.trade_f_dest_code_in:
        return True
    return False


def is_trade_i(origin_code, dest_code, shipment_type):
    if origin_code in Constant.trade_i_origin_code_in \
            and dest_code in Constant.trade_i_dest_code_in \
            and 'DISPOSAL' not in shipment_type.upper() \
            and 'CPU' not in shipment_type.upper():
        return True
    return False


def is_trade_n(origin_code, dest_code, shipment_type):
    if origin_code in Constant.trade_n_origin_code_in \
            and dest_code in Constant.trade_n_dest_code_in \
            and 'CPU' not in shipment_type.upper() \
            and 'DISPOSAL' not in shipment_type.upper():
        return True
    return False


def is_trade_o(origin_code, dest_code):
    if origin_code in Constant.trade_o_origin_code_in and \
            dest_code in Constant.trade_o_dest_code_in:
        return True
    return False


def is_trade_r(shipment_type):
    if 'RETURN' in shipment_type.upper() \
            or 'ASTRAY' in shipment_type.upper():
        return True
    return False


def is_trade_t(origin_code, dest_code):
    if origin_code in Constant.trade_t_origin_code_in \
            and dest_code not in Constant.trade_t_dest_code_not_in:
        return True
    return False


def is_trade_u(origin_code, shipment_type):
    if '1010' not in origin_code and \
            ('CPU' in shipment_type.upper() or \
             'CUSTOMER ROUTED' in shipment_type.upper()):
        return True
    return False


def is_trade_zc(origin_code, dest_code):
    if origin_code in Constant.trade_zc_origin_code_in and \
            dest_code not in Constant.trade_zc_dest_code_not_in:
        return True
    return False


def is_trade_zf(origin_code, dest_code):
    if origin_code in Constant.trade_zf_origin_code_in and \
            dest_code in Constant.trade_zf_dest_code_in:
        return True
    return False


def is_trade_zi(orign_code, dest_code):
    if orign_code in Constant.trade_zi_origin_code_in \
            and dest_code in Constant.trade_zi_dest_code_in:
        return True
    return False


def is_trade_zn(origin_code, dest_code):
    if 'TNJACAME001' in origin_code \
            and 'MNROCSEN002' in dest_code:
        return True
    return False


def is_trade_zo(origin_code, dest_code):
    if origin_code in Constant.trade_zo_origin_code_in \
            and dest_code in Constant.trade_zo_dest_code_in:
        return True
    return False


def is_trade_h():
    return True


def assign_flag(data_dict):
    origin_codes = data_dict['origin_code']
    dest_codes = data_dict['dest_code']
    shipment_types = data_dict['shipment_type']
    carrier_modes = data_dict['carrier_mode']

    trade_flags = list()

    for i, origin_code in enumerate(origin_codes):
        if is_trade_ac(origin_code, shipment_types[i]):
            trade_flags.append('AC')
        elif is_trade_ap(origin_code, carrier_modes[i]):
            trade_flags.append('AP')
        elif is_trade_u(origin_code, shipment_types[i]):
            trade_flags.append('U')
        elif is_trade_r(shipment_types[i]):
            trade_flags.append('R')
        elif is_trade_d(carrier_modes[i]):
            trade_flags.append('D')
        elif is_trade_f(origin_code, dest_codes[i]):
            trade_flags.append('F')
        elif is_trade_i(origin_code, dest_codes[i], shipment_types[i]):
            trade_flags.append('I')
        elif is_trade_c(origin_code, dest_codes[i], shipment_types[i]):
            trade_flags.append('C')
        elif is_trade_o(origin_code, dest_codes[i]):
            trade_flags.append('O')
        elif is_trade_n(origin_code, dest_codes[i], shipment_types[i]):
            trade_flags.append('N')
        elif is_trade_t(origin_code, dest_codes[i]):
            trade_flags.append('T')
        elif is_trade_zi(origin_code, dest_codes[i]):
            trade_flags.append('ZI')
        elif is_trade_zf(origin_code, dest_codes[i]):
            trade_flags.append('ZF')
        elif is_trade_zo(origin_code, dest_codes[i]):
            trade_flags.append('ZO')
        elif is_trade_zn(origin_code, dest_codes[i]):
            trade_flags.append('ZN')
        elif is_trade_zc(origin_code, dest_codes[i]):
            trade_flags.append('ZC')
        elif is_trade_h():
            trade_flags.append('H')

    data_dict['trade_flag'] = trade_flags
    return data_dict
