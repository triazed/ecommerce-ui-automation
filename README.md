## nopCommerce UI Test Automation
The project demonstrates automated UI testing using Selenium, Pytest and Page Object Model.

### Tech stack:
- Python
- Pytest
- Selenium WebDriver
- Page Object Model
- Docker / Docker Compose
- Chrome and Firefox

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
- config/          # URLs and framework configuration
- locators/        # Page and component locators
- pages/           # Page Objects and reusable UI components
- test_data/       # Test data and expected results
- tests/           # Pytest test suites and fixtures
- utils/           # Test data generators
- docker-compose.yml
- pytest.ini
- requirements.txt

### Design
The project follows the Page Object Model pattern.

- UI interactions are encapsulated in Page Objects and reusable components.
- Locators are separated from page logic.
- Pytest fixtures manage browser lifecycle and reusable test preconditions.
- Test data and expected results are separated from test logic.

### Prerequisites
- Python 3.10+
- Docker Desktop

### Install dependencies
`pip install -r requirements.txt`

### Environment Setup
Create a `.env` file in the project root based on `.env.example`:
`MSSQL_SA_PASSWORD=your_strong_password_here`

### Start test environment
`docker compose up -d`

### Initial nopCommerce setup
The test store will be available at:
`http://localhost:5000/install`

Use the following settings:
- Database type: SQL Server
- ✓ Create database if it doesn't exist 
- Server name: nop-db
- Database name: nopcommerce
- SQL Username: sa
- SQL Password: use the value from your `.env` file
- ✓ Enable sample data

### Launching tests
Chrome is used as the default browser.

`pytest` 

`pytest --browser=firefox`