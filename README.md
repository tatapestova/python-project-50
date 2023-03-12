### Hexlet tests and linter status:
[![Actions Status](https://github.com/tatapestova/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/tatapestova/python-project-50/actions)

### Codeclimate
<a href="https://codeclimate.com/github/tatapestova/python-project-50/maintainability"><img 
src="https://api.codeclimate.com/v1/badges/baa3a2b566dd0b9e965d/maintainability" /></a>
<a href="https://codeclimate.com/github/tatapestova/python-project-50/test_coverage"><img 
src="https://api.codeclimate.com/v1/badges/baa3a2b566dd0b9e965d/test_coverage" /></a>

### Github Actions Status
[![Python CI](https://github.com/tatapestova/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/tatapestova/python-project-50/actions/workflows/pyci.yml)

# FILE DIFF CALCULATOR

File diff calculator is a program that compares two files and outputs the result in three styles: 'stylish', 'plan' and 'json' (output examples are given below). 
Supported file formats for comparison - YAML, JSON.

## Used utilities

python = "^3.8.1"

pyyaml = "^6.0"

## Install
```
git clone https://github.com/tatapestova/python-project-50
```
```
pip install --user git+https://github.com/tatapestova/python-project-50
```

## Stylish style

The difference is built as a string, where the plus sign means that the key is in the first file, and the minus sign is in the second. If there is no additional sign before the key, the key is in both files.

### Flat files 

```bash
$ gendiff filepath1.json filepath2.json
```
[![asciicast](https://asciinema.org/a/EF3p0xMKmDP2SW40QwwmWszYG.svg)](https://asciinema.org/a/EF3p0xMKmDP2SW40QwwmWszYG)

```bash
$ gendiff filepath1.yml filepath2.yml
```
[![asciicast](https://asciinema.org/a/uB6FahjbBRlpnYbje2DsGml9V.svg)](https://asciinema.org/a/uB6FahjbBRlpnYbje2DsGml9V)

### Nested files

```bash
$ gendiff file1.json file2.json
```
[![asciicast](https://asciinema.org/a/hf2wK0VzvQHxMKkDo4rFBWvkf.svg)](https://asciinema.org/a/hf2wK0VzvQHxMKkDo4rFBWvkf)


```bash
$ gendiff file1.yml file2.yml
```
[![asciicast](https://asciinema.org/a/5rp4Z4wC5TFBlXxaVIeERezlP.svg)](https://asciinema.org/a/5rp4Z4wC5TFBlXxaVIeERezlP)

## Plain style

The difference is built as a string, where the text reflects the situation, as if we combined the second object with the first.
If the key value is complex, then the resulting line will contain [complex value].

### Flat files

```bash
$ gendiff --format plain filepath1.yml filepath2.yml
```

[![asciicast](https://asciinema.org/a/fKseZnYBCKwIEaWP9YNPCtapk.svg)](https://asciinema.org/a/fKseZnYBCKwIEaWP9YNPCtapk)

### Nested files

```bash
$ gendiff --format plain file1.json file2.json
```
[![asciicast](https://asciinema.org/a/rmvvkaIHdgAWkyH5RyFaMoV8d.svg)](https://asciinema.org/a/rmvvkaIHdgAWkyH5RyFaMoV8d)

## JSON style

The difference is built in JSON format, where each node is added to its stratus. The logic of the status is that as if we have combined the second object with the first. 

### Flat files 

```bash
$ gendiff --format json filepath1.json filepath2.json
```

[![asciicast](https://asciinema.org/a/rxIiDwWoY3jGnvSvxUhXJfY80.svg)](https://asciinema.org/a/rxIiDwWoY3jGnvSvxUhXJfY80)

### Nested files

```bash
$ gendiff --format json file1.json file2.json
```
[![asciicast](https://asciinema.org/a/HPC4LXtehAFdYDW8nTH4xVAGK.svg)](https://asciinema.org/a/HPC4LXtehAFdYDW8nTH4xVAGK)
