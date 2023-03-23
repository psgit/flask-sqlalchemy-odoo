# Flask SQLAlchemy Odoo

SQLAlchemy + Flask Tutorial

Documentation : https://docs.graphene-python.org/projects/sqlalchemy/en/latest/tutorial/

To start the app in Windows PowerShell, enter:
python app.py

In the browser, enter the following URL: 
http://localhost:5000/graphq

Example Queries:

{
  allPartners {
    edges {
      node {
        id
        name
      }
    }
  }
}


{
  allUsers {
    edges {
      node {
        id
        login
        partner {
          name
        }
      }
    }
  }
}