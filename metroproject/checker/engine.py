import datetime as dt


def find_rota_details(given_date=(dt.datetime.now()).isoformat()):
    rota_length = 126
    parsed_date = dt.datetime.fromisoformat(given_date)
    searched_duties = []
    initial = dt.datetime(2020, 1, 11)
    tdelta = parsed_date - initial
    diff = tdelta.days % rota_length
    week = diff//7
    day_no = diff % 7
    return Rota.objects.all()

