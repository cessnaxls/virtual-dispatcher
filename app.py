from flask import Flask, render_template, request
import random
import datetime


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


def format_minutes(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours:02d}:{mins:02d}"


@app.route('/', methods=['GET', 'POST'])
def home():
    trip = []
    airports = ['IND', 'ATL', 'DFW', 'ORD', 'CLT']

    FAA_7DAY_LIMIT = 1800  # 30h
    FAA_28DAY_LIMIT = 6000  # 100h

    if request.method == 'POST':
        selected_airlines = request.form.getlist('airlines')
        airlines = selected_airlines if selected_airlines else NA_ICAO_AIRLINES

        selected_aircraft = request.form.getlist('aircraft')
        aircraft = selected_aircraft if selected_aircraft else ICAO_AIRCRAFT_TYPES

        initial_departure = request.form.get('initial_departure', '').strip().upper()
        include_airports = [a.strip().upper() for a in request.form.get('include_airports', '').split(',') if a.strip()]
        exclude_airports = [a.strip().upper() for a in request.form.get('exclude_airports', '').split(',') if a.strip()]

        if include_airports:
            airports = list(set(airports + include_airports))
        if exclude_airports:
            airports = [a for a in airports if a not in exclude_airports]
        if initial_departure and initial_departure not in airports:
            airports.append(initial_departure)

        start_date_str = request.form.get('start_date')
        end_date_str = request.form.get('end_date')
        availability_str = request.form.get('availability')

        max_legs = int(request.form.get('max_legs', 4))
        max_flight_minutes = int(request.form.get('max_flight_hours', 8)) * 60

        available_dates = set()
        if availability_str:
            ranges = availability_str.split(',')
            for part in ranges:
                try:
                    start_str, end_str = part.strip().split(' to ')
                    start = datetime.datetime.strptime(start_str.strip(), '%Y-%m-%d').date()
                    end = datetime.datetime.strptime(end_str.strip(), '%Y-%m-%d').date()
                    for n in range((end - start).days + 1):
                        available_dates.add(start + datetime.timedelta(days=n))
                except Exception as e:
                    print(f"Error parsing range '{part}': {e}")
        elif start_date_str and end_date_str:
            start = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()
            for n in range((end - start).days + 1):
                available_dates.add(start + datetime.timedelta(days=n))

        day_counter = 1
        last_arrival = initial_departure if initial_departure else random.choice(airports)

        total_legs_count = 0
        total_flight_minutes_all = 0
        total_off_days = 0

        prior_day_end_time = None
        day_flight_times = {}  # {date: minutes}

        for leg_date in sorted(available_dates):
            legs_today = []
            total_flight = 0
            num_legs = random.randint(1, max_legs)
            max_duty_for_day = 840 if num_legs <= 4 else 720

            # Calculate rolling past days
            past_7 = [leg_date - datetime.timedelta(days=i) for i in range(1, 8)]
            past_28 = [leg_date - datetime.timedelta(days=i) for i in range(1, 29)]
            rolling_7day = sum(day_flight_times.get(d, 0) for d in past_7)
            rolling_28day = sum(day_flight_times.get(d, 0) for d in past_28)

            if rolling_7day >= FAA_7DAY_LIMIT or rolling_28day >= FAA_28DAY_LIMIT:
                trip.append({
                    'day': day_counter,
                    'date': leg_date.strftime('%Y-%m-%d'),
                    'airline': 'OFF',
                    'aircraft': 'OFF',
                    'dep': 'OFF',
                    'arr': 'OFF',
                    'dep_time': 'OFF',
                    'arr_time': 'OFF'
                })
                total_off_days += 1
                prior_day_end_time = None
                day_flight_times[leg_date] = 0
                day_counter += 1
                continue

            dep_minute_of_day = 360  # ~6am

            for _ in range(num_legs):
                if total_flight >= max_flight_minutes:
                    break

                dep_airport = last_arrival
                arr_choices = [a for a in airports if a != dep_airport]
                if include_airports:
                    arr_choices = [a for a in arr_choices if a in include_airports]
                if exclude_airports:
                    arr_choices = [a for a in arr_choices if a not in exclude_airports]
                if not arr_choices:
                    arr_choices = airports

                arr_airport = random.choice(arr_choices)
                flight_time = random.randint(60, 300)

                # Check rolling FAA limits
                if (rolling_7day + total_flight + flight_time > FAA_7DAY_LIMIT or
                    rolling_28day + total_flight + flight_time > FAA_28DAY_LIMIT):
                    break

                arr_minute_of_day = dep_minute_of_day + flight_time

                leg = {
                    'day': day_counter,
                    'date': '',
                    'airline': random.choice(airlines),
                    'aircraft': random.choice(aircraft),
                    'dep': dep_airport,
                    'arr': arr_airport,
                    'dep_time': format_minutes(dep_minute_of_day),
                    'arr_time': format_minutes(arr_minute_of_day)
                }
                legs_today.append(leg)

                total_flight += flight_time
                dep_minute_of_day = arr_minute_of_day + 60  # add ~1h turn
                last_arrival = arr_airport

            if legs_today:
                total_legs_count += len(legs_today)
                total_flight_minutes_all += total_flight
                day_flight_times[leg_date] = total_flight

                # Calculate prior rest
                if prior_day_end_time is not None:
                    prior_rest = max(0, (24 * 60 + 360) - prior_day_end_time)
                else:
                    prior_rest = 720  # first day

                prior_day_end_time = arr_minute_of_day

                trip.append({
                    'day': day_counter,
                    'date': leg_date.strftime('%Y-%m-%d'),
                    'airline': 'SUMMARY',
                    'aircraft': '',
                    'dep': '',
                    'arr': '',
                    'dep_time': f'Flight: {format_minutes(total_flight)}',
                    'arr_time': f'Duty: {format_minutes(total_flight + len(legs_today) * 60)}',
                    'total_legs': len(legs_today),
                    'prior_rest': format_minutes(prior_rest)
                })
                trip.extend(legs_today)
            else:
                prior_day_end_time = None
                total_off_days += 1
                day_flight_times[leg_date] = 0
                trip.append({
                    'day': day_counter,
                    'date': leg_date.strftime('%Y-%m-%d'),
                    'airline': 'OFF',
                    'aircraft': 'OFF',
                    'dep': 'OFF',
                    'arr': 'OFF',
                    'dep_time': 'OFF',
                    'arr_time': 'OFF'
                })

            day_counter += 1

        total_duty_minutes_all = total_flight_minutes_all + total_legs_count * 60

        summary = {
            'total_legs': total_legs_count,
            'total_flight': format_minutes(total_flight_minutes_all),
            'total_duty': format_minutes(total_duty_minutes_all),
            'rolling_7day': format_minutes(sum(day_flight_times.get(d, 0) for d in past_7)),
            'rolling_28day': format_minutes(sum(day_flight_times.get(d, 0) for d in past_28)),
            'off_days': total_off_days
        }

    else:
        summary = None

    return render_template('index.html', trip=trip,
                           NA_ICAO_AIRLINES=NA_ICAO_AIRLINES,
                           ICAO_AIRCRAFT_TYPES=ICAO_AIRCRAFT_TYPES,
                           summary=summary)
