import os

# Path to temporary directory within the mounted tmpfs
tmp_dir = "/app/tmp"

def process_sensitive_data(data):
    # Ensure the temporary directory exists.
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)

    # Write sensitive data to a temporary file within the mounted tmpfs
    with open(os.path.join(tmp_dir, "sensitive_data.txt"), "w") as f:
        f.write(data)
    
    # Perform processing on the sensitive data
    with open(os.path.join(tmp_dir, "sensitive_data.txt"), "r") as f:
        processed_data = f.read()
        print(f"Processed Data: {processed_data}")

# Example usage
data_to_process = "This is sensitive data by TheToriqul, please enjoy you practice!"
process_sensitive_data(data_to_process)
