# EU Digital COVID Certificate Decoder
This is a couple of scripts for dumping out the contents of the [EU Digital COVID Certificate](https://ec.europa.eu/info/live-work-travel-eu/coronavirus-response/safe-covid-19-vaccines-europeans/eu-digital-covid-certificate_en). It doesn't perform any sort of verification or validation.

The field names for the JSON message are abbreviated, you can find the schema therefor on the [ehn-dcc-development project](https://github.com/ehn-dcc-development/ehn-dcc-schema/blob/release/1.3.0/DCC.combined-schema.json).

## Requirements
System requirements:

- `zbar-tools` for reading the QR code
- `python3` for running the python script

Python packages needed:

- `base45` for decoding the QR code's content into the [CBOR](https://cbor.io/) message
- `flynn` for unpacking the CBOR message


## Running
```
$ ./read-qr.sh < QR_CODE.png
```
