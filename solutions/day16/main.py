import os
import math
import binascii
from types import coroutine
from bitarray import bitarray

def get_example_input():
    s = """D2FE28""" # Number Example
    s = """38006F45291200""" # Operator Example with length_in_bits
    s = """EE00D40C823060""" # Operator Example with length in amount
    s = """8A004A801A8002F478""" # Version sum 16
    s = """620080001611562C8802118E34""" # Version sum 12
    s = """C0015000016115A2E0802F182340""" # Version sum 23
    s = """A0016C880162017C3686B18A3D4780""" # Version sum 31
    s = """C200B40A82""" # Sum 1 + 2 = 3
    s = """04005AC33890""" # prod 6*9 = 54
    s = """880086C3E88112""" # min(7,8,9) = 7
    s = """CE00C43D881120""" # max(7,8,9) = 9
    s = """D8005AC2A8F0""" # 5<15 = 1
    s = """F600BC2D8F""" # 5>15 = 0
    s = """9C005AC2F8F0""" # 5==15 = 0
    s = """9C0141080250320F1802104A08""" # 1+3 == 2*2 -> 1
    return s.splitlines()

def get_input():
    with open('solutions/day16/input.txt') as f:
        return [x.strip() for x in f.readlines()]

def unhexify(_string):
    return binascii.unhexlify(_string)

def consume(_bits):
    return _bits.pop(0)

def consume_n(_bits, n):
    b = bitarray()
    for _ in range(n):
        b.append(consume(_bits))
    return b

def get_version(_bits):
    return consume_n(_bits, 3)

def get_packet_type(_bits):
    return consume_n(_bits, 3)

def convert_to_number(_bits):
    return int(_bits.to01(), 2)

def parse_literal(_bits):
    leading = consume(_bits)
    amount_consumed = 7
    number_bits = bitarray()
    while leading > 0:
        number_bits.extend(consume_n(_bits, 4))
        leading = consume(_bits)
        amount_consumed += 5
    number_bits.extend(consume_n(_bits, 4))
    amount_consumed += 4
    while not amount_consumed % 4 == 0:
        amount_consumed += 1
    number = convert_to_number(number_bits)
    return number

def parse_operator(_bits, packet_type_number):
    length_type_id = consume(_bits)
    length_length = 15 if length_type_id == 0 else 11
    length = convert_to_number(consume_n(_bits, length_length))
    children = []
    if length_type_id == 1:
        for _ in range(length):
            children.append(parse_packet(_bits))
    else:
        current_bits_length = len(_bits)
        while len(_bits) > current_bits_length - length:
            children.append(parse_packet(_bits))
    match packet_type_number:
        case 0:
            return sum(children)
        case 1:
            return math.prod(children)
        case 2:
            return min(children)
        case 3:
            return max(children)
        case 5:
            return int(children[0] > children[1])
        case 6:
            return int(children[0] < children[1])
        case 7:
            return int(children[0] == children[1])
    

_all_version_numbers = 0

def parse_packet(_bits):
    global _all_version_numbers
    version = get_version(_bits)
    version_number = convert_to_number(version)
    _all_version_numbers += version_number
    packet_type_number = convert_to_number(get_packet_type(_bits))
    if packet_type_number == 4:
        number = parse_literal(_bits)
    else:
        number = parse_operator(_bits, packet_type_number)
    return number


def task1():
    number = unhexify(get_input()[0])
    bits = bitarray()
    bits.frombytes(number)
    parse_packet(bits)
    return _all_version_numbers

def task2():
    number = unhexify(get_input()[0])
    bits = bitarray()
    bits.frombytes(number)
    return parse_packet(bits)
