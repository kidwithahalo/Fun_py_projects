def parse_values(data_line):
    values = []
    for item in data_line.strip().split(','):
        if item == '':
            values.append((0.0))
        else:
            values.append(float(item))

    return values