from . import argument_parser
from . import calculator
from . import formatter
from . import loader


def main():
  parser = argument_parser.get_parser()
  args = parser.parse_args()

  data = loader.load_input_data(args.filename)

  fed_withholding = calculator.get_fed_withholding(data)
  ca_withholding = calculator.get_ca_withholding(data)

  fed_tax = calculator.get_fed_tax(data, fed_withholding.tax, ca_withholding.tax)
  ca_tax = calculator.get_ca_tax(data, ca_withholding.tax)

  output = formatter.format(data, fed_withholding, ca_withholding, fed_tax, ca_tax)
  print(output)


if __name__ == '__main__':
  main()
