import yaml

from . import model


def maybe_sum(value):
  if isinstance(value, (int, float)):
    return value
  elif isinstance(value, list):
    return sum(value)
  elif isinstance(value, dict):
    return sum(value.values())
  else:
    raise ValueError(
        f'Value type must be one of (int, float, list, dict): value={value}, type={type(value)}')


def input_data_yaml_constructor(loader, node):
  raw_dict = loader.construct_mapping(node, deep=True)

  fields = {key: maybe_sum(value) for key, value in raw_dict.items()}
  fields['filing_status'] = model.FilingStatus(fields['filing_status'])

  return model.InputData(**fields)


def load_input_data(filename):
  tag = '!InputData'
  yaml.add_constructor(tag, input_data_yaml_constructor, Loader=yaml.SafeLoader)

  with open(filename, 'r') as in_file:
    content = in_file.read()

  data = yaml.safe_load(content)

  if not isinstance(data, model.InputData):
    raise ValueError(f"Unexpected type loaded (is file missing '{tag}' tag?): {type(data)}")

  return data
