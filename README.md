# estimated-taxes

Estimated taxes calculator.

This is meant to help estimate additional tax payments throughout the year, i.e.
for [IRS form 1040-ES](https://www.irs.gov/pub/irs-pdf/f1040es.pdf) and [CA form
540-ES](https://www.ftb.ca.gov/forms/2019/19_540es.pdf).

Please review the logic yourself if you intend to use this. It intentionally
does not attempt to handle all forms and all scenarios; you will likely need to
augment it for your particular needs.

See also [nkouevda/capital-gains](https://github.com/nkouevda/capital-gains).

## Installation

    pip install estimated-taxes

## Usage

```
usage: estimated-taxes [<options>] [--] <input file>

Estimated taxes calculator

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
```

## Input Format

See [example/input.yaml](example/input.yaml).

The input file must start with `!InputData`, and must specify `year`,
`filing_status`, `fed_allowances`, and `ca_allowances`. All other values are
optional.

Each value must be a number, or a list of numbers, or a map where the values are
numbers. Lists and maps are allowed for convenience, to split up categories into
multiple entries. For example, the following are all equivalent:

```
supplemental_wages: 62500

supplemental_wages:
  - 12500
  - 50000

supplemental_wages:
  bonus: 12500
  rsu: 50000
```

## Examples

    estimated-taxes example/input.yaml > example/output.txt

## TODO

- Itemized deductions other than SALT
- AMT

## License

[MIT License](LICENSE.txt)
