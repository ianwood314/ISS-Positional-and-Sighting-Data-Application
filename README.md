# ISS Positional and Sighting Data Application

The purpose of this application is to provide the user with various positional and sightings data for the International Space Station (ISS).
Specifically, the user can access information related to the postion and velocity of the ISS at specific times as well as the country, region, or city
the ISS was sighted in at specific times.

NOTE: for the sections below, a port number of 5038 is used.

## How to Download the Pre-built Code
1. Pull the image from Docker Hub
    - Type `make pull` in the command line
    - Alteratively, you can type `docker pull ianwood314/iss-data-query:1.1` in the command line (which is the same command executed by `make pull`)
2. Run the image
    - Type `make run` in the command line
    - Alternatively, type `docker run --name "iss-query-data" -d -p 5038:5000 ianwood314/iss-data-query:1.1` (again, the same command executed by `make run`)
3. Now that you have the image up and running, see the [How to Interact with the Application](#how-to-interact-with-the-application) section for a list of queryable routes

## How to Build Your Own Image
1. Download the Necessary Files
    - Clone this repository using `git clone` to access all files required to build the image (learn how to clone a repository [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository))
2. Build the image from the Dockerfile
    - `NAME="<username>" make build`
    - Alternatively, type `docker build -t <username>/iss-data-query:<tag> .` (remember to replace with your own username and tag)
3. Download the data 
    - Required data files: `ISS.OEM_J2K_EPH.xml` and `XMLsightingData_citiesUSA01.xml` (a description of these files is available in the [Data Files](#data-files) section)
    - Download the data [here](https://data.nasa.gov/Space-Science/ISS_COORDS_2022-02-13/r6u8-bhhq)
      - `ISS.OEM_J2K_EPH.xml`: under link "Public Distribution"
      - `XMLsightingData_citiesUSA01.xml`: under link "XMLsightingData_citiesUSA01"
5. Run the image
    - `NAME="<username>" make run`
    - Alternatively, type `docker run --name "iss-query-data" -d -p 5038:5000 <username>/iss-data-query:1.1`
6. Now that you have the image up and running, see the section below for a list of queryable routes

## How to Interact with the Application

#### View a list of all the queryable routes
  - `curl localhost:5038`
  - Once you run the command above, you should see the following output:
    ```
    -- How to Interact with this Application --

    In order to access the data, you must first download it:
       curl localhost:<your port #>/download-data -X POST

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
      10. /sightings/city-<city>
    ```
  - Ouput above details how to download the data and provides a list of the ten queryable routes

#### Brief description of each queryable route
1. `/epochs`
    - Returns a list of dictionaries where each dictionary is an epoch
2. `/epochs/<requested_epoch>`
    - Takes in user input of an epoch and returns the first dictionary whose EPOCH key value matches the user's input
3. `/sightings`: 
    - Returns a list of dictionaries where each dictionary is a sighting of the ISS
4. `/sightings/countries`
    - Returns a list of dictionaries where each dicationary is a country along with the numer of times a sighting occured in that country
5. `/sightings/<country>`
    - Takes in a country as user input and returns a list of dictionaries where each dictionary is a sighting in that country
6. `/sightings/countries/regions`
    - Returns a dictionary where the keys are all of the countries in the sightings data and the values are a list of the regions where a sighting occured in that country
7. `/sightings/<country>/regions`
    - Takes in a country as user input and returns a dictionary where the first and only key is the country given and the value is a list of dictionaries where each dictionary is a region with the number of sightings within that region
8. `/sightings/region-<region>`
    - Takes in a region as user input and returns a list of dictionaries where wach dictionary is a sighting in the region provided by the user
9. `/sightings/<country>-<region>-cities`
    - Takes a country and region as user input and returns a dictionary where the key is the country provided and the value is another dictionary where the first key value-pair is the region provided and the second key-value pair are the cities located in that country and region
10. `/sightings/city-<city>`
    - Takes in a city name as user input and returns a dictionary where they key is the city provided and the value is a list of all the data for sightings in that city


  
## Interpret the Results
1. `/epochs`
2. `/epochs/<requested_epoch>`
3. `/sightings`
4. `/sightings/countries`
5. `/sightings/<country>`
6. `/sightings/countries/regions`
7. `/sightings/<country>/regions`
8. `/sightings/region-<region>`
9. `/sightings/<country>-<region>-cities`
10. `/sightings/city-<city>`

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
