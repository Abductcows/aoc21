from utils import get_lines, get_input_for_day

BITS_PER_BUCKET = 64
BITS_PER_WORD = 4
WORDS_PER_BUCKET = BITS_PER_BUCKET // BITS_PER_WORD


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


def run(lines):
    data, total_bits = pack(lines[0])
    total_bits -= 3

    version_sum = 0

    cur = 0
    while cur < total_bits:
        version, cur = consume(data, cur, 3)
        type_id, cur = consume(data, cur, 3)
        if type_id == 4:  # literal
            literal_value = 0
            while True:
                part, cur = consume(data, cur, 5)
                partial_value = part & 0xf
                literal_value = (literal_value << 4) + partial_value
                if not part & 0x10:
                    break
        else:  # operator packet
            length_type_id, cur = consume(data, cur, 1)
            if length_type_id == 0:
                _trash, cur = consume(data, cur, 15)
            else:
                _trash, cur = consume(data, cur, 11)

        version_sum += version

    return version_sum


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d16')))
