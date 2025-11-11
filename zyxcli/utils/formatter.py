def simple_table(headers, rows):
    widths = [len(h) for h in headers]
    for r in rows:
        for i, c in enumerate(r):
            widths[i] = max(widths[i], len(str(c)))
    sep = ' | '
    hdr = sep.join(h.ljust(widths[i]) for i,h in enumerate(headers))
    lines = [hdr, '-+-'.join('-'*w for w in widths)]
    for r in rows:
        lines.append(sep.join(str(c).ljust(widths[i]) for i,c in enumerate(r)))
    return '\n'.join(lines)
