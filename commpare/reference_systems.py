import importlib

### Identify the reference systems for which to evaluate energy
def identify_reference_systems():
    reference_systems = []
    if detect_validate():
        reference_systems.append('validate')
    if detect_foyer():
        reference_systems.append('foyer')
    if detect_mbuild():
        reference_systems.append('mbuild')

    return reference_systems

def detect_validate():
    try:
        importlib.import_module('validate')
        return True
    except ModuleNotFoundError:
        return False

def detect_foyer():
    try:
        importlib.import_module('foyer')
        return True
    except ModuleNotFoundError:
        return False

def detect_mbuild():
    try:
        importlib.import_module('mbuild')
        return True
    except ModuleNotFoundError:
        return False
