from flask import Flask, render_template, request
import random

app = Flask(__name__)

NA_ICAO_AIRLINES = [
    'AAH', 'AAL', 'AAY', 'ABK', 'ABX', 'ACA', 'ADS', 'AER', 'AIE', 'AIP', 'AJI',
    'AJT', 'AKN', 'AKT', 'AMF', 'AMX', 'ANT', 'ARQ', 'ASA', 'ASB', 'ASH', 'ASP',
    'ATN', 'AWI', 'AXT', 'BBA', 'BBQ', 'BFF', 'BFL', 'BHR', 'BLS', 'BMG', 'BMJ',
    'BRG', 'BTQ', 'BXH', 'BYA', 'BZQ', 'CAV', 'CBF', 'CDN', 'CFS', 'CHI', 'CJT',
    'CKS', 'CNK', 'CNS', 'CPT', 'CRE', 'CRN', 'CRQ', 'CRR', 'CSB', 'CSJ', 'CSQ',
    'CSX', 'CVU', 'CWA', 'CWH', 'DAL', 'DCX', 'DHC', 'DRL', 'EAL', 'EDV', 'EJA',
    'ENY', 'ERM', 'ESF', 'EUS', 'EXA', 'FDX', 'FDY', 'FEX', 'FFT', 'FGD', 'FJA',
    'FLE', 'FLL', 'FRG', 'FSY', 'FTO', 'GGN', 'GHK', 'GJS', 'GLR', 'GMT', 'GPD',
    'GSL', 'GTI', 'GUE', 'GUN', 'GXA', 'HAL', 'HES', 'HKA', 'HMB', 'HRT', 'HYD',
    'IFL', 'IRO', 'JBA', 'JBU', 'JIA', 'JSN', 'JSX', 'JUD', 'JUS', 'JZA', 'KAP',
    'KBA', 'KEN', 'KEW', 'KFA', 'KFS', 'KNT', 'KUK', 'KYE', 'LBR', 'LCT', 'LET',
    'LRT', 'LSJ', 'LVW', 'LYC', 'LYM', 'MAA', 'MAL', 'MAX', 'MBI', 'MBK', 'MCS',
    'MEI', 'MFC', 'MGE', 'MHO', 'MRA', 'MTN', 'MUI', 'MXA', 'MXY', 'NAC', 'NAL',
    'NCB', 'NCR', 'NDL', 'NEA', 'NKS', 'NLF', 'NLI', 'NOJ', 'NRL', 'NTA', 'NTG',
    'NVC', 'NWL', 'OAE', 'ONT', 'PAC', 'PAG', 'PBR', 'PCM', 'PCO', 'PDT', 'PHA',
    'PHX', 'PLR', 'PNO', 'POE', 'PRD', 'PRO', 'PSC', 'PUL', 'PVL', 'PWC', 'PXT',
    'QUE', 'QXE', 'RAG', 'RAX', 'RDB', 'RFD', 'RLI', 'ROD', 'ROU', 'RPA', 'RSP',
    'RTD', 'RTU', 'RVF', 'RYA', 'SCE', 'SCX', 'SDE', 'SEE', 'SEN', 'SJN', 'SKL',
    'SKW', 'SKZ', 'SLG', 'SLI', 'SLQ', 'SMX', 'SNC', 'SPA', 'SPR', 'SST', 'SUT',
    'SWA', 'SYB', 'TGO', 'THU', 'TIN', 'TLK', 'TNO', 'TOR', 'TPM', 'TQN', 'TSC',
    'TTU', 'TXG', 'TXH', 'UAL', 'UCA', 'UJC', 'UPS', 'URF', 'USC', 'VAL', 'VIV',
    'VKN', 'VOI', 'VOS', 'VTE', 'VTM', 'VTS', 'VXP', 'WAL', 'WAV', 'WEN', 'WGN',
    'WIG', 'WJA', 'WRF', 'WSG', 'WSN', 'WWW', 'XLS', 'XOJ', 'XSR'
]

ICAO_AIRCRAFT_TYPES = [
    'A124', 'A140', 'A148', 'A158', 'A19N', 'A20N', 'A21N', 'A225', 'A306',
    'A30B', 'A310', 'A318', 'A319', 'A320', 'A321', 'A332', 'A333', 'A337',
    'A338', 'A339', 'A342', 'A343', 'A345', 'A346', 'A359', 'A35K', 'A388',
    'A3ST', 'A400', 'A748', 'AC90', 'AJ27', 'AN12', 'AN24', 'AN26', 'AN28',
    'AN30', 'AN32', 'AN72', 'AT43', 'AT45', 'AT46', 'AT72', 'AT73', 'AT75',
    'AT76', 'ATP', 'B190', 'B37M', 'B38M', 'B39M', 'B3XM', 'B461', 'B462',
    'B463', 'B52', 'B703', 'B712', 'B720', 'B721', 'B722', 'B732', 'B733',
    'B734', 'B735', 'B736', 'B737', 'B738', 'B739', 'B741', 'B742', 'B743',
    'B744', 'B748', 'B74R', 'B74S', 'B752', 'B753', 'B762', 'B763', 'B764',
    'B772', 'B773', 'B778', 'B779', 'B77L', 'B77W', 'B788', 'B789', 'B78X',
    'BA11', 'BCS1', 'BCS3', 'BE20', 'BE40', 'BE99', 'BELF', 'BER2', 'BLCF',
    'C130', 'C212', 'C25A', 'C25B', 'C25C', 'C30J', 'C5M', 'C500', 'C510',
    'C525', 'C550', 'C560', 'C56X', 'C650', 'C680', 'C68A', 'C700', 'C750',
    'C919', 'CL2T', 'CL30', 'CL60', 'CN35', 'CRJ1', 'CRJ2', 'CRJ7', 'CRJ9',
    'CRJX', 'CVLT', 'D228', 'D328', 'DC10', 'DC85', 'DC86', 'DC87', 'DC91',
    'DC92', 'DC93', 'DC94', 'DC95', 'DH8A', 'DH8B', 'DH8C', 'DH8D', 'DHC5',
    'DHC6', 'DHC7', 'E110', 'E120', 'E135', 'E145', 'E170', 'E190', 'E195',
    'E290', 'E295', 'E35L', 'E50P', 'E545', 'E550', 'E55P', 'E75L', 'E75S',
    'EA50', 'F100', 'F27', 'F28', 'F2TH', 'F406', 'F50', 'F70', 'F900',
    'FA50', 'FA6X', 'FA7X', 'G159', 'G280', 'G73T', 'GL5T', 'GLEX', 'GLF4',
    'GLF5', 'GLF6', 'GA7C', 'H25B', 'H25C', 'HDJT', 'I114', 'IL18', 'IL62',
    'IL76', 'IL86', 'IL96', 'J328', 'JS31', 'JS32', 'JS41', 'K35R', 'L101',
    'L188', 'L410', 'LJ35', 'LJ60', 'MD11', 'MD81', 'MD82', 'MD83', 'MD87',
    'MD88', 'MD90', 'MU2', 'N262', 'NOMA', 'P8', 'P180', 'PAY2', 'PC24',
    'RJ1H', 'RJ70', 'RJ85', 'S601', 'SB20', 'SC7', 'SF34', 'SH33', 'SH36',
    'SU95', 'SW4', 'T134', 'T154', 'T204', 'WW24', 'Y12', 'YK40', 'YK42',
    'YS11'
]

@app.route('/', methods=['GET', 'POST'])
def home():
    trip = []
    airports = ['IND', 'ATL', 'DFW', 'ORD', 'CLT']

    if request.method == 'POST':
        selected_airlines = request.form.getlist('airlines')
        airlines = selected_airlines if selected_airlines else NA_ICAO_AIRLINES

        selected_aircraft = request.form.getlist('aircraft')
        aircraft = selected_aircraft if selected_aircraft else ICAO_AIRCRAFT_TYPES

        for day in range(1, 6):
            dep_airport = random.choice(airports)
            arr_airport = random.choice([ap for ap in airports if ap != dep_airport])
            leg = {
                'day': day,
                'airline': random.choice(airlines),
                'aircraft': random.choice(aircraft),
                'dep': dep_airport,
                'arr': arr_airport,
                'dep_time': f"{random.randint(5, 22)}:{random.randint(0,59):02d}",
                'arr_time': f"{random.randint(5, 22)}:{random.randint(0,59):02d}"
            }
            trip.append(leg)

    return render_template('index.html', trip=trip,
                           NA_ICAO_AIRLINES=NA_ICAO_AIRLINES,
                           ICAO_AIRCRAFT_TYPES=ICAO_AIRCRAFT_TYPES)

if __name__ == '__main__':
    app.run(debug=True)