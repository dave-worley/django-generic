# Product Catalog

I elected to work on the Product Catalog utility project. The project was created using Python 3.4 and Django 1.8. Installation instructions follow the project features.

My Product Catalog has the following features:

   - Displays a formatted list of products.
   - The list of products paginates.
   - Users can add a new product using a web based form.
   - Users can add multiple products at once using a CSV file upload tool.
   - Users can delete products.
   - Users can edit existing products.

According to the Extra Credit I've added the following additional features:

   - Users can place an order for a product from the product detail page. Orders are associated with an existing product in the database.
   - When an order is placed the user's address is verified using Google's geocoding service. The validation is basic but effective.
   - When an order is successfully placed the user is redirected to a simple order detail view.

I've tried for a fairly production ready system. Some caveats:

   - There is no user authentication. Any user is a superuser. This was a design choice based on time constraints. Implementing Django's authentication is trivial but involves a lot of boilerplate that I felt would distract from the core application features.
   - There is no way to view a list of existing orders. There is no way to navigate to an existing order in the UI. Orders are stored in the database. This was also a choice based on time.
   - The UI is primitive and based on simple Bootstrap defaults. As far as programmer designed UI goes it's not half bad.

## Installation

_Disclaimer: This process will not work on Windows. You are not using Windows I bet._

1. Download the repo.
   > git clone https://github.com/dave-worley/shipwire-project.git

2. Use Python 3.4. Install a virtualenv.
   > virtualenv venv

3. Activate the virtual environment.
   > source venv/bin/activate

4. Install the dependencies with pip. This will install Django in the virtualenv.
   > pip install -r requirements.txt

5. Change to the ProductCatalog directory.
   > cd ProductCatalog

6. Run the Django migration commands to create the sqlite database.
   > python manage.py makemigrations
   > python manage.py migrate

7. You're all set. Run the Django development server.
   > python manage.py runserver
