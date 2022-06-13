# Documentation

This is a Restful API about anime streaming created using **Python**.

## Demo

<#>
Comming Soon

## Requirements
- Git
- Python 3
- Pip3

## Installation

```
git clone https://github.com/fikrifirmanf/animerestapi-python.git
cd animerestapi-python
pip3 install -r requirements.txt
```

### Running on Dev Mode

```
python3 manage.py runserver
```

### Status Code

#### Response Code

```
200: Success
302: Moved
500: Internal Server Error
```

## REST API

GET <http://localhost:8000/api/v1/anime/search?q=bor> --> Search anime

GET <http://localhost:8000/api/v1/anime/ddd-episode-6-sub-indo/stream> --> Getting anime streaming link

GET <http://localhost:8000/api/v1/anime/dance-danseur-sub-indo/detail> --> Getting anime detail

GET <http://localhost:8000/api/v1/anime?page=1&filter_by=on-going> --> Getting anime category on-going/complete

## Data Source

<https://otakudesu.watch/>

### NOT FOR COMMERCIAL

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by-nc-sa/4.0/)