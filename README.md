# Licmon backend

Backend application of the Licmon website. Parses information from the [Flex server](https://www.flexnetmanager.com/) queries.


## Installation

To start a development server execute the commands below

Install the requirements

`pip3 install -r requirements.txt`

Run a local server

`python3 app.py`


## Usage

A request to the server can be sent as shown below

`http://localhost:5000/product/<application>`

i.e. `http://localhost:5000/product/comsol`

The response will have the following structure

```json
{
  "name": "string",
  "features": [
    {
      "name": "string",
      "version": "string",
      "vendor": "string",
      "licenses_issued": 0,
      "licenses_in_use": 0,
      "users": [
        {
          "username": "string",
          "hostname": "string",
          "display": "string",
          "version": "string",
          "server": "string",
          "port": "string",
          "handle": "string",
          "checkout": "string",
          "num_licenses": "string"
        }
      ],
      "message": "string"
    }
  ]
}
```
