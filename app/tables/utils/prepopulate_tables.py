import csv

from tables.models import Table

with open('tables/utils/prepopulate_tables_input.csv') as f:
    for row in csv.reader(f, delimiter='\t'):
        Table.objects.create(
            category=row[0],
            name=row[1],
            url=row[2],
        )
