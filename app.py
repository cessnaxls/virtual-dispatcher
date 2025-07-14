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

@app.route('/', methods=['GET', 'POST'])
def home():
    trip = []
    aircraft = ['B737', 'B757', 'CRJ700']
    airports = ['IND', 'ATL', 'DFW', 'ORD', 'CLT']

    if request.method == 'POST':
        selected_airlines = request.form.getlist('airlines')
        airlines = selected_airlines if selected_airlines else NA_ICAO_AIRLINES

        for day in range(1, 6):
            leg = {
                'day': day,
                'airline': random.choice(airlines),
                'aircraft': random.choice(aircraft),
                'dep': random.choice(airports),
                'arr': random.choice([ap for ap in airports if ap != 'IND']),
                'dep_time': f"{random.randint(5, 22)}:{random.randint(0,59):02d}",
                'arr_time': f"{random.randint(5, 22)}:{random.randint(0,59):02d}"
            }
            trip.append(leg)

    return render_template('index.html', trip=trip, NA_ICAO_AIRLINES=NA_ICAO_AIRLINES)

if __name__ == '__main__':
    app.run(debug=True)
