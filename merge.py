import pathlib
import csv
import pyaml
import yaml


source_path = "mini-cards.csv"
target_path = pathlib.Path("cards.yaml")


target_raw = target_path.read_text()
target = yaml.load(target_raw, yaml.Loader)

with open(source_path) as csvfile:
    reader = csv.DictReader(csvfile)
    for mini_card in reader:
        name = mini_card["Name"]
        if name not in target:
            print(f"Skipping {name}")
            continue
        primary = mini_card["Primary Function"]
        secondary = mini_card.get("Secondary Function")
        function = primary
        if secondary:
            function += f"\n\n{secondary}"
        target[name]["Function"] = function

target_path.write_text(pyaml.dump(target))
