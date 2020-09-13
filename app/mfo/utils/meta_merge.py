import json

from mfo.models import Lender

with open('mfo/utils/meta_merge_input/fin_mfos.json') as f:
    for l in json.load(f):
        # print(l)
        cbrn = l.get('reg_number', '')
        if len(cbrn) == 15:
            cbrn = cbrn[2:]
        lender = Lender(
            scraped_from=['https://www.cbr.ru/vfs/finmarkets/files/supervision/list_MFO.xlsx'],
            id_meta=l['id'],
            cbrn=cbrn or '',
            ogrn=str(l.get('ogrn')) or '',
            inn=str(l.get('inn')) or '',
            trademark=l.get('name') or '',
            name_full=l.get('full_name') or '',
            head_name=l.get('head_name') or '',
            address=l.get('address') or '',
            email=l.get('email') or '',
            is_legal=(not bool(l.get('is_illegal', False))),
        )
        lender.save()
