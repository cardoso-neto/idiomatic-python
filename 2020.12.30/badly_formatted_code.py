
# it is better to ask for forgivennes than for permission

def is_ok(old_thread) -> bool:
    return old_thread.get('archive-chan', {}).get('images', {}).get('is_file_present', False)
def is_ok(old_thread) -> bool:
    try:
        return old_thread["archive-chan"]["images"]["is_file_present"]
    except KeyError:
        return False



def very_important_function(template: str, *variables, file: os.PathLike, engine: str, header: bool = True, debug: bool = False):
    """Applies `variables` to the `template` and writes to `file`."""
    with open(file, 'w') as f:
        ...

j = [1,
     2,
     3
]

ImportantClass.important_method(exc, limit, lookup_lines, capture_locals, extra_argument)
