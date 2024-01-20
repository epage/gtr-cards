import pathlib
import pyaml
import csv


in_path = "cards.csv"
out_path = "cards.yaml"
with open(in_path) as csvfile:
    reader = csv.DictReader(csvfile)

    output = {}
    for card in reader:
        name = card["Structure"]
        del card["Structure"]

        for field in ["Value", "Card Count"]:
            value = card[field]
            value = int(value)
            card[field] = value

        output[name] = card

    output = pyaml.dump(output)
    pathlib.Path(out_path).write_text(output)

