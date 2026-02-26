badge_records = [
  ["Martha",   "exit"],
  ["Paul",     "enter"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "enter"],
  ["Paul",     "enter"],
  ["Curtis",   "enter"],
  ["Paul",     "exit"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "exit"],
]


def get_anamolies_from_badge_records(badge_records: List):
    in_room = set()
    invalid_entries = set()
    invalid_exits = set()
    for items in badge_records:
        if items[1] == 'enter':
            if items[0] in in_room:
                invalid_entries.add(items[0])
            in_room.add(items[0])
        else:
            if items[0] not in in_room:
                invalid_exits.add(items[0])
            else:
                in_room.remove(items[0])
    invalid_entries.update(in_room)
            
    return [invalid_entries,invalid_exits]



print(get_anamolies_from_badge_records(badge_records))
