# ISS Positional and Sighting Data Application

The purpose of this application is to provide the user with various positional and sightings data for the International Space Station (ISS).
Specifically, the user can access information related to the postion and velocity of the ISS at specific times as well as the country, region, or city
the ISS was sighted in at specific times.

## How to Download the Pre-built Code



## How to Build Your Own Image




## How to Interact with the Application



## Interpret the Results



## Scripts
1. `app.py`
  - Main application script 
  - Contains POST endpoint to load the data into memory in order to query the data
  - Contains all the GET routes the user can use to query data
3. `test_app.py`
  - Tests all routes in the previous script for error handling

## Data Files
1. `ISS.OEM_J2K_EPH.xml`
  - Contains the specific, time, position, and velocity data for the ISS
2. `XMLsightingData_citiesUSA01.xml`
  - Contains the sightings of the ISS within the United States
  - Contains the specifc time, country (United States), region (state), and city the sighitng took place

The ISS data above was taken from NASA's official website found [here](https://data.nasa.gov/Space-Science/ISS_COORDS_2022-02-13/r6u8-bhhq).

## How to Run the Test Suite with Pytest
