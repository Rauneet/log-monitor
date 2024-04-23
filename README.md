# log-monitor script
This script monitors specified log files for new entries and counts occurrences of a user-defined regex pattern. It is useful for tracking specific errors or events in application logs in real-time.

# Prerequisites
* Python 3.x Make sure that python3 is installed in your system. You can download it from [python.org](https://www.python.org/) .
* Operating system This script is used for Unix like OS due to file handling methods used.

# Dependencies
No external dependencies is required except the Python Standard Library. 

# Setup 
* Clone the repository or download the script file **log-monitoring.py** to your local machine.
* Ensure you have access to the log file taht you wish to monitor.This file should be in a location that the script can read from.

# Usuage 
To use the script follow these steps:
1. Open the terminal.
2. Navigate to the directory which contains the script.
3. Run the script with the following command format:
   `python log-monitoring.py <log_file_path> <pattern_to_search>`
        * `<log_file_path>` absolute or relative path of the log file which you need to monitor.
        * `<pattern_to_search>` Regex pattern to look for in the log file (e.g., "ERROR", "404", etc.).
   Example:
   `python log-monitoring.py /path/to/your/logfile.log "error|ERROR|404"`

# Testing 
1. Start the script as described above.
2. Append entries to your log file.
     * You can manually add entries that match and do not match the pattern to see if the script picks up and counts the entries     
       correctly.Use the following command to append to a log file:
       `echo "2024-01-01 12:00:00 ERROR Something went wrong" >> /path/to/your/logfile.log`
3. Observe the output
     * The script prints each line it reads and counts occurrences of the pattern, reporting the counts every 10 lines.
4. **interupt the script** by pressing Ctrl+C to test graceful shutdown.

# Logging 
* The script logs all operations, including starts, stops, and errors, to a file named log-monitor.log. Check this log file for a detailed operational trace.
# Error Handling 
* The script includes basic error handling for file access and regex operations.
       `
