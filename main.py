import argparse
import time
import threading

# Global flag for system state
SYSTEM_RUNNING = False

def scrape_bestsellers():
    """Continuously scrapes bestseller data until stopped."""
    while SYSTEM_RUNNING:
        print("Scraping best-selling products from top dropshipping sites...")
        time.sleep(10)  # Simulate scraper execution
        if not SYSTEM_RUNNING:
            break
    print("Scraping stopped.")

def start_system():
    global SYSTEM_RUNNING
    if SYSTEM_RUNNING:
        print("System is already running.")
        return
    SYSTEM_RUNNING = True
    print("Starting AI-powered bestseller scraping...")
    scraper_thread = threading.Thread(target=scrape_bestsellers)
    scraper_thread.start()

def stop_system():
    global SYSTEM_RUNNING
    SYSTEM_RUNNING = False
    print("Stopping bestseller scraping...")

def resume_system():
    global SYSTEM_RUNNING
    if SYSTEM_RUNNING:
        print("System is already running.")
        return
    start_system()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI-Powered Bestseller Scraping System")
    parser.add_argument("command", choices=["start", "stop", "resume"], help="Control system operation")
    args = parser.parse_args()

    if args.command == "start":
        start_system()
    elif args.command == "stop":
        stop_system()
    elif args.command == "resume":
        resume_system()
