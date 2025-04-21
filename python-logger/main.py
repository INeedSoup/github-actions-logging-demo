import time
import logging
import random

# Configure logging
logging.basicConfig(
    filename='output.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def simulate_process():
    for i in range(5):
        try:
            logging.info(f'Processing step {i+1}/5...')
            if random.random() < 0.2:  # 20% chance to fail
                raise ValueError("Random error occurred!")
            time.sleep(1)
        except Exception as e:
            logging.error(f"Error in step {i+1}: {str(e)}")
            return False
    logging.info('Process completed successfully.')
    return True

if __name__ == '__main__':
    logging.info('Script started.')
    success = simulate_process()
    logging.info(f'Script ended. Success: {success}')
    exit(0 if success else 1)  # Exit code for GitHub Actions
