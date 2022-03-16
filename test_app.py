from app import *
from flask import jsonify
import pytest

help_str = '''\n-- How to Interact with this Application --\n
In order to access the data, you must first download it:
  curl localhost:<your port #>/download-data -X POST\n
Once the data is downloaded, you can access it through the following routes:
  1.  /epochs
  2.  /epochs/<requested_epoch>
  3.  /sightings
  4.  /sightings/countries
  5.  /sightings/<country>
  6.  /sightings/countries/regions
  7.  /sightings/<country>/regions
  8.  /sightings/region-<region>
  9.  /sightings/<country>-<region>-cities
  10. /sightings/city-<city>\n\n'''
output_error_str = '\n-- Data Variables Not Defined --\n\nPlease first download the data using:\n  curl localhost:5038/download-data -X POST\n\n'
filenotfound_error_str = '\n-- File not Found --\n\n'

def test_help():
	assert help() == help_str

def test_download_data():
	assert download_data() == '\n-- Download Successful --\n\n'
	assert download_data(iss_pos_filename = 'random.xml', sightings_filename = 'XMLsightingData_citiesUSA01.xml') == filenotfound_error_str + 'The ISS positional data XML file was not\n\n'
	assert download_data(iss_pos_filename = 'ISS.OEM_J2K_EPH.xml', sightings_filename = 'random.xml') == filenotfound_error_str + 'The ISS sightings data XML file was not\n\n'

def test_get_epochs():
	assert get_epochs() == output_error_str

def test_get_epoch():
	assert get_epoch('abc') == '  Epoch abc not found\n'

def test_get_sightings():
	assert get_sightings() == output_error_str

def test_get_countries():
	assert get_countries() == output_error_str

def test_get_country():
	assert get_country('zootopia') == output_error_str

def test_get_regions_of_countries():
	assert get_regions_of_countries() == output_error_str

def test_get_regions_of_country():
	assert get_regions_of_country('transformers') == output_error_str

def test_get_region():
	assert get_region('oz') == output_error_str

def test_get_cities():
	assert get_cities('merica','myhometown') == output_error_str

def test_get_city():
	assert get_city('perfectplaces') == output_error_str
