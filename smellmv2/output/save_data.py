import os
import datetime
class SaveData():
    def __init__(self):
        curr_dir = os.path.dirname(__file__)
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        
        # Create the output directory name
        output_dir_name = f"output-{timestamp}"
        
        # Create the full path for the output directory
        self.output_dir_path = os.path.join(curr_dir, output_dir_name)
        if not os.path.exists(self.output_dir_path):
            os.makedirs(self.output_dir_path)
            print(f"Created output directory: {self.output_dir_path}")
            
    def save_file(self, data):
        
        for key, value in data.items():
            # Replace any / or \ in the key with _
            safe_filename = key.replace('/', '_').replace('\\', '_')
            
            if '.' in safe_filename:
                filename_base = safe_filename.rsplit('.', 1)[0]  # Get the name without extension
                safe_filename = f"{filename_base}.md"
            else:
                safe_filename = f"{safe_filename}.md"
            
            # Create the full path to the file
            file_path = os.path.join(self.output_dir_path, safe_filename)
            
            # Write the data to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(value)
            
            print(f"Saved data to {file_path}")
        
        return self.output_dir_path