from os.path import join, dirname
from json import loads
from jsonschema import validate


def asert_valid_schema(data, schema_file):
    """
    Checks whether the given data matches the schema.
    """
    schema = _load_json_schema(schema_file)
    return validate(data, schema)


def _load_json_schema(filename):
    """
    Loads the given schema file.
    """
    relative_path = join('schema', filename)
    absolute_path = join(dirname(dirname(__file__)), relative_path)

    with open(absolute_path) as schema_file:
        return loads(schema_file.read())
