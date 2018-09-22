from os.path import join, dirname
from jsonschema import validate
from jsonref import loads


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
    relative_path = join("schemas", filename)
    absolute_path = join(dirname(dirname(__file__)), relative_path)

    base_path = dirname(absolute_path)
    base_uri = f"file://{base_path}/"

    with open(absolute_path) as schema_file:
        return loads(schema_file.read(), base_uri=base_uri, jsonschema=True)
