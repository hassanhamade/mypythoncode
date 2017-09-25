from datetime import datetime
def parse_date(s,fmt):
    try:
        ret=datetime.strptime(s,fmt)
    except ValueError:
        ret=datetime.now()
    return ret
