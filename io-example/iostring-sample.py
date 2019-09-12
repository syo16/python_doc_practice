import io

output = io.StringIO()
output.write('First line\n')
print('Second line.', file=output)

contents = output.getvalue()

print(contents)
output.close()
