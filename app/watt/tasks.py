import csv
import os

from app.watt.models import Item


def import_csv(filename):
    if not os.path.isfile(filename):
        return 0

    # clear database
    Item.objects.all().delete()

    # import
    files_created_count = 0
    with open(filename, "rt") as f:
        reader = csv.reader(f)
        next(reader, None)  # skip the headers
        for row in reader:
            try:
                item = Item(
                    name=row[0],
                    wh_per_unit=int(row[2]),
                    energy_type=row[4],
                    unit=row[3],
                    default_usage=float(row[5]),
                    source=row[6]
                )

                item.save()
                files_created_count += 1
            except:
                pass

    return files_created_count
