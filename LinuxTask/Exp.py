import json
import os
import re
import subprocess
import sys

import jsondiff
import jsonschema

DEPENDENCY_KEY = "dependencies"
version_schema = re.compile(r"(?:(\d+\.[.\d]*\d+))")
schema = {
    "type": "object",
    "properties": {
        "dependencies": {
            "type": "object"
        },
    },
    "required": ["dependencies"]
}


def install(package, ins_flag=True):
    op = "install" if ins_flag else "uninstall"
    try:
        subprocess.check_call([sys.executable, "-m", "pip", op, package])
    except Exception as e:
        e.__str__()
        print(f"Failed to {op} {package}")


if not os.path.exists("./.temp"):
    open(".temp", "w+", encoding="utf-8").close()


def check():
    with open("requirements.json", "r") as new_require, open(".temp", "r", encoding="utf-8") as old_require:
        temp = old_require.read()
        prev = json.loads(temp) if temp else None
        curr: dict = json.load(new_require)
        skiplist = list()
        jsonschema.validate(curr, schema)
        for k, v in curr.get(DEPENDENCY_KEY).items():
            if not version_schema.match(v):
                print(f"Version incorrect -> {k}:{v}. Skipping")
                skiplist.append(k)
        if not prev:
            diff = curr
            print("No change")
            open(".temp", "w").write(json.dumps(curr))
        else:
            diff = jsondiff.diff(prev, curr)
            print("Change detected.")
        if diff:
            for d, v in diff.get(DEPENDENCY_KEY).items():
                if str(d) not in ["$delete", "replace"] + skiplist:
                    install(d + '==' + v)
                # Uncomment to add uninstall feature when a dependency is removed from the requirements.
                # else:
                #     install(" ".join(v), ins_flag=False)
            curr: str = json.dumps(prev)
            open(".temp", "w").write(curr)


if __name__ == "__main__":

    # Uncomment to run continuously
    # UPDATE_RATE = 5  # Seconds
    # while 1:
    #     check()
    #     time.sleep(UPDATE_RATE)
    check()
