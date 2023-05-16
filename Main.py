import openpyxl


with open('example.txt', 'r') as file:
    content = file.readlines()

workbook = openpyxl.Workbook()

worksheet = workbook.active

worksheet.append(['Code', 'Ack', 'Cause', 'Description', 'Domain', 'Severity', 'Last Transition'])

code = ''
ack = ''
cause = ''
description = ''
domain = ''
severity = ''
last_transition = ''

for line in content:

    if line.startswith('code'):
        code = line.split(': ')[1].strip()

    elif line.startswith('ack'):
        ack = line.split(': ')[1].strip()

    elif line.startswith('cause'):
        cause = line.split(': ')[1].strip()

    elif line.startswith('descr'):
        description = line.split(': ')[1].strip()

    elif line.startswith('domain'):
        domain = line.split(': ')[1].strip()

    elif line.startswith('severity'):
        severity = line.split(': ')[1].strip()

    elif line.startswith('lastTransition'):
        last_transition = line.split(': ')[1].strip()
        worksheet.append([code, ack, cause, description, domain, severity, last_transition])
        code = ''
        ack = ''
        cause = ''
        description = ''
        domain = ''
        severity = ''
        last_transition = ''

workbook.save('example.xlsx')