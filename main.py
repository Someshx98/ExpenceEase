from tracker import ExpenseTracker
import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('expense_tracker.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)


def main():
    try:
        logger.info("Starting Expense Tracker application")
        app = ExpenseTracker()
        app.menu()
        logger.info("Expense Tracker application closed")
    
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user.")
        logger.info("Application interrupted by user")
        sys.exit(0)
    
    except Exception as e:
        print(f"\n✗ An unexpected error occurred: {e}")
        logger.error(f"Unexpected error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()