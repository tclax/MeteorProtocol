import sys
from binascii import hexlify, unhexlify

if __name__ == "__main__":
    filename = sys.argv[1]

    data = None

    with open(filename, 'rb') as f:
        data = f.read()


    packet_data_pos = 8

    header = data[0:packet_data_pos]
    print(f'header: {header}')
    number_of_packets = int(header[0:4],16)
    packet_size = int(header[4:6],16)
    modulation_factor = int(header[6:8],16)

    print(f'number of packets: {number_of_packets}')
    print(f'packet_size: {packet_size}')
    print(f'modulation_factor: {modulation_factor}')

    packet_dict = {}

    for packet_number in range(0, number_of_packets):
        packet_data = data[packet_data_pos:packet_data_pos+packet_size]
        print(f'packet_data: {packet_data}')

        packet_index = int(packet_data[0:2], 16)
        print(f'packet_index: {packet_index}')

        packet_payload = packet_data[2:]
        packet_dict[packet_index] = packet_payload

        packet_data_pos += packet_size
    
    print(f'packet_dict: {packet_dict}')

    sorted_dict = dict(sorted(packet_dict.items(), key=lambda item: item[1]))

    print(f'sorted dict: {sorted_dict}')

    keyphrase = b''
    for value in sorted_dict.values():
        keyphrase += value
    
    print(f'final keyphrase: {unhexlify(keyphrase)}')


    




