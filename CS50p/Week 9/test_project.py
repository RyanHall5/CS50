from project import get_num, read_data, get_runner
from project import runners_lists
import operator
import csv


def test_get_num(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1")
    assert get_num() == 1
    monkeypatch.setattr('builtins.input', lambda _: "100")
    assert get_num() == 100

def test_read_data():
    in_file = open("data.csv")
    file = csv.DictReader(in_file)
    read_data(file)
    assert runners_lists["all"]["all"][1].name == "neil harrington"
    assert runners_lists["all"]["9"][0].name == "jack alves"

def test_get_runner():
    in_file = open("data.csv")
    file = csv.DictReader(in_file)
    read_data(file)
    for gen_list in runners_lists.values():
        for grade_list in gen_list.values():
            grade_list.sort(key=operator.attrgetter('pr_seconds'))

    assert get_runner(1,"m","all").name == "neil harrington"
    assert get_runner(1,"f","all").name == "sydney o'donnell"
    assert get_runner(1000,"all","all") == "No Runner exists at that rank"

