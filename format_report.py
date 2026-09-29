part_name = "  hydraulic-value-4  "
pressure = 45.6789

cleaned_part_name = part_name.strip().replace("-", " ").upper()
output_text = f"The {cleaned_part_name} operates at {pressure:.1f} bar."

print(output_text)