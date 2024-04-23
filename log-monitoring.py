#necessary imports
import logging
import re
import time
import signal
import sys

#configuring the basic logging to write the message with the timestamp to a file 
logging.basicConfig(filename='log-monitor.log', level= logging.DEBUG, format='%(asctime)s %(message)s')

#Function to handle interrupt signals, logs information and exits cleanly
def signal_handler(sig,frame):
    logging.info('Intrupt received...Monitoring stopped')
    print('Intruppt received.. Stopping monitoring')
    sys.exit(0)

#Registering the signal handler function for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

#Generator function that simulates the Unix 'tail -f' command
def tail_f(file):
    with open(file, 'r') as f:
        #Move to the end of the file
        f.seek(0,2)
        while True:
            line = f.readline()
            #If no new line is available, sleep briefly and try again
            if not line:
                time.sleep(1)
                continue
            yield line

#Counts the occurrences of a regex pattern in given lines
def count_occureneces(lines, pattern):
    count = 0 
    for line in lines:
        if re.search(pattern, line):
            count += 1
    return count

#Main function to monitor the log file and count occurrences of a pattern
def log_monitor(file_path, pattern):
    try:
        logging.info('Starting log monitoring.')
        print(f'Monitoring {file_path} for few entries')
        lines_checked = 0 
        pattern_count = 0 
        for line in tail_f(file_path):
            lines_checked +=1
            print(line, end='')
            if re.search(pattern, line):
                pattern_count +=1
            #Log the count of pattern matches every 10 lines
            if lines_checked % 10 == 0:
                logging.debug(f'Checked {lines_checked} lines so far, pattern {pattern_count} matches found for pattern {pattern}.')
    except Exception as e:
         #Log and print any exceptions that occur during monitoring
        logging.error(f'An error occured: {str(e)}')
        print(f'An error occured: {str(e)}')

if __name__ == '__main__':
    #Ensure that the script is run with exactly two additional command line arguments
    if len(sys.argv) != 3:
        print("Usage: python log-monitor.py <log_file_path> <pattern_to_search>")
        sys.exit(1)
    log_file_path = sys.argv[1]
    search_pattern = sys.argv[2]
    log_monitor(log_file_path, search_pattern)


