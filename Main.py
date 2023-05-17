import csv

with open('example.txt', 'r') as file:
    content = file.read()

# Split the content into individual fault.Inst sections
fault_insts = content.split('# fault.Inst')

# Remove empty fault.Inst sections
fault_insts = [fault_inst for fault_inst in fault_insts if fault_inst.strip()]

# Get all unique field names
field_names = set()
for fault_inst in fault_insts:
    lines = fault_inst.strip().split('\n')
    for line in lines:
        if ':' in line:
            field = line.split(':')[0].strip()
            field_names.add(field)

# Create a CSV file for the output
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()

    # Process each fault.Inst section
    for fault_inst in fault_insts:
        # Create a dictionary to store the field values
        field_data = {}

        # Split the fault.Inst section into lines
        lines = fault_inst.strip().split('\n')

        # Extract the field name-value pairs
        for line in lines:
            if ':' in line:
                field, value = line.split(':', 1)
                field = field.strip()
                value = value.strip()
                field_data[field] = value

        # Write the field values to the CSV file
        writer.writerow(field_data)
