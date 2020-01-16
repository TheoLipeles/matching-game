from django import template
import os, json
register = template.Library()

with open(os.path.join(os.getcwd(), 'boxes.json')) as json_file:
    boxes = json.load(json_file)

@register.inclusion_tag('_delayed_next.html')
def delayed_next(wait=2000, label="NEXT"):
    return {
        "wait": wait,
        "label": label
    }

@register.inclusion_tag('_matching_box.html')
def matching_box(choices=["...","...","...","...",0,"...","...","...","..."], matching_box_id="matching_box", rounds=1):
    return {
        "choices": choices,
        "matching_box_id": matching_box_id,
        "rounds": rounds,
        "boxes": boxes
    }
