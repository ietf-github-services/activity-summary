#!/usr/bin/env python3

"""
Summarise activity using Dom's github-notify-ml script.

This is really just glue between it and repo_data.json.
"""

import json


def createMls(repo_data, override=None):
    out = {}
    for group in repo_data:
        for repo_name in repo_data[group].get("repos", {}):
            repo = repo_data[group]["repos"][repo_name]
            for recipient in repo.get("activity_summary_to", []):
                if override:
                    recipient = override
                elif recipient == "group_email":
                    recipient = repo_data[group].get("email", None)
                    if recipient is None:
                        sys.stderr.write(
                            f"WARNING: unknown recipient {recipient}; skipping.\n"
                        )
                        continue
                if recipient not in out:
                    out[recipient] = {
                        "digest:sunday": {
                            "topic": f"{repo_data[group].get('group_name', '')} Activity Summary",
                            "repos": [],
                            "eventFilter": {},
                        }
                    }
                out[recipient]["digest:sunday"]["repos"].append(repo_name)
                if "activity_exclude_labels" in repo_data[group]:
                    out[recipient]["digest:sunday"]["eventFilter"] = {
                        "notlabel": repo_data[group]["activity_exclude_labels"]
                    }
    return out


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="List activity.")
    parser.add_argument("repo_data_file", help="The repo_data.json file location")
    parser.add_argument("--override", action="store", help="Override e-mail for testing")
    args = parser.parse_args()

    with open(args.repo_data_file) as repo_data_fh:
        repo_data = json.load(repo_data_fh)
    mls = createMls(repo_data, args.override)
    print(json.dumps(mls, indent=4, sort_keys=True))
