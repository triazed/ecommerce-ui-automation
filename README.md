### UI test automation project for nopCommerce demo store.
The project demonstrates automated UI testing using Selenium, Pytest and Page Object Model.

### Tech stack:
- Python
- Pytest
- Selenium
- Page Object Model
- Docker (for local test environment)

### Test coverage
The project covers the following user flows:

- User registration (positive and negative scenarios)
- User login (positive and negative scenarios)
- Product search (dropdown and search results)
- Cart operations (add, remove, quantity validation)
- Checkout flow (guest and authorized user)

End-to-end flow:
search → add to cart → cart → checkout → order

### Project structure
- pages/ – Page Object Model implementation
- locators/ – UI locators
- tests/ – test scenarios
- test_data/ – test data and expectations
- utils/ – data generators

### Prerequisites
- Python 3.10+
- Docker Desktop

### Start test environment
docker compose up -d

### Initial setup
The test store will be available at:
http://localhost:5000/install

Use the following settings:
- Database type: SQL Server
- ✓ Create database if it doesn't exist 
- Server name: nop-db
- Database name: nopcommerce
- SQL Username: sa
- SQL Password: (see docker-compose.yml)
- ✓ Enable sample data

### Install dependencies
pip install -r requirements.txt

### Launching tests
Chrome is used as the default browser.

pytest 

pytest --browser=firefox