# Iran IP List

IPv4 ranges allocated to Iran, generated from RIPEstat country resources.

## Usage

Use the raw `ipv4.txt` file directly:

```text
https://raw.githubusercontent.com/aminvakil/ir-ip-list/refs/heads/main/ipv4.txt
```

Or watch repository releases to be notified when `ipv4.txt` changes.

## Files

- `ipv4.txt`: Iran IPv4 prefixes, one CIDR per line.

## Source

Data is fetched from RIPEstat:

```text
https://stat.ripe.net/data/country-resource-list/data.json?resource=ir
```

## Generate

```bash
curl -s "https://stat.ripe.net/data/country-resource-list/data.json?resource=ir" \
  | jq -r '.data.resources.ipv4[]' \
  | python split_subnets.py > ipv4.txt
```

`split_subnets.py` converts IPv4 ranges returned by RIPEstat into CIDR blocks. Existing CIDR lines are kept unchanged.

## Updates

GitHub Actions checks RIPEstat daily and opens a pull request when `ipv4.txt` changes.

Releases are created when changes to `ipv4.txt` are merged into `main`.
