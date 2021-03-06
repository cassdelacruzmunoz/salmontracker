import sys

sys.path.insert(0, ".")
import core
from objects import Job
import ujson
import gzip
from typing import Dict


data = core.init("All", "data/")
eventDict: Dict[str, dict] = {
    "None": {"key": "none", "count": 0.0},
    "mothership": {"key": "mothership", "count": 0.0},
    "fog": {"key": "fog", "count": 0.0},
    "rush": {"key": "rush", "count": 0.0},
    "cohock_charge": {"key": "cohock_charge", "count": 0.0},
    "griller": {"key": "griller", "count": 0.0},
    "goldie_seeking": {"key": "goldie_seeking", "count": 0.0},
}
total = 0.0
with gzip.open(data) as reader:
    for line in reader:
        job = Job(**ujson.loads(line))
        for wave in job.waves:
            total += 1.0
            if wave.known_occurrence is not None:
                eventDict[wave.known_occurrence.key]["count"] += 1.0
            else:
                eventDict["None"]["count"] += 1.0
for event in eventDict.values():
    print(event["key"] + ": " + str(event["count"] / total))
