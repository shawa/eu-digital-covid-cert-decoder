import base45
import flynn
import json
import sys
import zlib

def zlib_blob_for(qr_code_content):
    OFFSET = 4

    base45_blob = qr_code_content[OFFSET:]
    zlib_data = base45.b45decode(base45_blob)

    return zlib_data

def cbor_message_for(zlib_blob):
    uncompressed = zlib.decompress(zlib_blob)
    cbor_message = flynn.decoder.loads(uncompressed)
    return cbor_message

def payload_for(cbor_message):
    (_, (_, _, signed_message, _signature)) = cbor_message
    return flynn.decoder.loads(signed_message)

def main():
    qr_code_content = sys.stdin.read()
    zlib_blob = zlib_blob_for(qr_code_content)
    cbor_message = cbor_message_for(zlib_blob)
    payload = payload_for(cbor_message)
    output = json.dumps(payload)

    sys.stdout.write(output)

if __name__ == '__main__':
    main()
