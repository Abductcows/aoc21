from functools import reduce

from utils import get_lines, get_input_for_day

BITS_PER_BUCKET = 64
BITS_PER_WORD = 4
WORDS_PER_BUCKET = BITS_PER_BUCKET // BITS_PER_WORD

type_ids = {'literal': 4, 'sum': 0, 'product': 1, 'min': 2, 'max': 3, 'gt': 5, 'lt': 6, 'eq': 7}


def pack(data):
    buckets = []
    total_bit_length = 0

    for i in range(0, len(data), WORDS_PER_BUCKET):
        shift = BITS_PER_BUCKET - BITS_PER_WORD
        slice = data[i:i + WORDS_PER_BUCKET]
        packed = 0
        for word in slice:
            total_bit_length += BITS_PER_WORD
            packed |= int(word, 16) << shift
            shift -= BITS_PER_WORD
        buckets.append(packed)

    return buckets, total_bit_length


def select_bits(num, start, nbits, right_align=False):
    left_cleared = ((num << start) & ((1 << BITS_PER_BUCKET) - 1)) >> start
    if right_align:
        return left_cleared >> BITS_PER_BUCKET - start - nbits
    return left_cleared >> BITS_PER_BUCKET - start - nbits << BITS_PER_BUCKET - start - nbits


def consume(data, cur, nbits):
    assert nbits <= WORDS_PER_BUCKET
    bucket, index = divmod(cur, BITS_PER_BUCKET)

    if nbits + index <= BITS_PER_BUCKET:
        return select_bits(data[bucket], index, nbits, right_align=True), cur + nbits

    if bucket + 1 >= len(data):
        raise ValueError('Tried to consume out of <data> array bounds')

    first_bucket_nbits = BITS_PER_BUCKET - index
    first_part = select_bits(data[bucket], index, first_bucket_nbits, right_align=True)

    second_bucket_nbits = nbits - first_bucket_nbits
    second_part = select_bits(data[bucket + 1], 0, second_bucket_nbits, right_align=True)

    return (first_part << second_bucket_nbits) | second_part, cur + nbits


def resolve_children(cur, data):
    length_type_id, cur = consume(data, cur, 1)
    children_values = []
    if length_type_id == 0:
        children_nbits, cur = consume(data, cur, 15)
        start = cur
        while cur < start + children_nbits:
            child_value, cur = resolve_packet_value(data, cur)
            children_values.append(child_value)
    else:
        child_count, cur = consume(data, cur, 11)
        for _ in range(child_count):
            child_value, cur = resolve_packet_value(data, cur)
            children_values.append(child_value)
    return children_values, cur


def resolve_literal_packet(cur, data):
    literal_value = 0
    while True:
        part, cur = consume(data, cur, 5)
        partial_value = part & 0xf
        literal_value = (literal_value << 4) + partial_value
        if not part & 0x10:
            return literal_value, cur


def resolve_packet_value(data, cur):
    version, cur = consume(data, cur, 3)
    type_id, cur = consume(data, cur, 3)

    if type_id == type_ids['literal']:
        return resolve_literal_packet(cur, data)

    children_values, cur = resolve_children(cur, data)

    if type_id == type_ids['sum']:
        return sum(children_values), cur
    if type_id == type_ids['product']:
        return reduce(lambda acc, v: acc * v, children_values), cur
    if type_id == type_ids['min']:
        return min(children_values), cur
    if type_id == type_ids['max']:
        return max(children_values), cur
    if type_id == type_ids['gt']:
        return int(children_values[0] > children_values[1]), cur
    if type_id == type_ids['lt']:
        return int(children_values[0] < children_values[1]), cur
    if type_id == type_ids['eq']:
        return int(children_values[0] == children_values[1]), cur


def run(lines):
    data, total_bits = pack(lines[0])
    total_bits -= 3
    return resolve_packet_value(data, 0)[0]


if __name__ == '__main__':
    print(run(['C200B40A82']))  # 3
    print(run(['04005AC33890']))  # 54
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d16')))
