# Flask SQLAlchemy Odoo

SQLAlchemy + Flask Tutorial

Documentation : https://docs.graphene-python.org/projects/sqlalchemy/en/latest/tutorial/

## Installing Requirements

To install requirements the app in Windows PowerShell, enter:
```
  pip install -r requirements.txt
```

## Configuring the Database Connection

In the **db.cfg** file, configure the postgresql connection string to connect to your Odoo database:
```
[Database]
connect_string = postgresql://[user]:[password]@localhost:5432/[database]
```

## Starting the Application

To start the app in Windows PowerShell, enter:
```
  python app.py
```

## Querying with GraphQL

In the browser, enter the following URL: 
  http://localhost:5000/graphq

### Example Queries

#### Query All Partners

```
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
```

#### Query All Users

```
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
```
