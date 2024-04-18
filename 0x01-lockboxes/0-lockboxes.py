#!/usr/bin/python3
""" def function canUnlockAll """


def canUnlockAll(boxes):
    """ method that determines if all the boxes can be opened """
    box_keys = set([0] + boxes[0])
    locked = set()
    for box in boxes:
        ibox = boxes.index(box)
        if ibox not in box_keys:
            if max(box_keys) > ibox:
                locked.add(ibox)
                continue
        box_keys |= set(box)
    for key in locked:
        if key in box_keys:
            box_keys |= set(boxes[key])
    return not bool(locked - box_keys)
