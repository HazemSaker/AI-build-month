def group_by(rows: list, key: str) -> list:
    """ grouping rows by a key, return list of dicts grouped by the key."""
    groups = {}

    for row in rows:
        if row[key] not in groups:
            groups[row[key]] = []

        groups[row[key]].append(row)

    return groups