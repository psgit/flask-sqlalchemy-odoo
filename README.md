# GraphQL Flask SQLAlchemy Odoo

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

In this project the [GraphQL](https://graphql.org/) support is provided by [graphene-sqlalchemy](https://docs.graphene-python.org/projects/sqlalchemy/en/latest/starter/) which in turn uses [Graphene Pyhton](https://graphene-python.org/) and [SQLAlchemy](https://www.sqlalchemy.org/).

### Example Queries

#### Query the Schema
```
{
  __schema {
    queryType {
      fields {
        name
      }
    }
  }
}
```
#### Query the whole Schema
You could use the following query found in [stackoverflow - Get GraphQL whole schema query](https://stackoverflow.com/questions/37397886/get-graphql-whole-schema-query)
```
query IntrospectionQuery {
  __schema {
    queryType {
      name
    }
    mutationType {
      name
    }
    subscriptionType {
      name
    }
    types {
      ...FullType
    }
    directives {
      name
      description
      locations
      args {
        ...InputValue
      }
    }
  }
}

fragment FullType on __Type {
  kind
  name
  description
  fields(includeDeprecated: true) {
    name
    description
    args {
      ...InputValue
    }
    type {
      ...TypeRef
    }
    isDeprecated
    deprecationReason
  }
  inputFields {
    ...InputValue
  }
  interfaces {
    ...TypeRef
  }
  enumValues(includeDeprecated: true) {
    name
    description
    isDeprecated
    deprecationReason
  }
  possibleTypes {
    ...TypeRef
  }
}

fragment InputValue on __InputValue {
  name
  description
  type {
    ...TypeRef
  }
  defaultValue
}

fragment TypeRef on __Type {
  kind
  name
  ofType {
    kind
    name
    ofType {
      kind
      name
      ofType {
        kind
        name
        ofType {
          kind
          name
          ofType {
            kind
            name
            ofType {
              kind
              name
              ofType {
                kind
                name
              }
            }
          }
        }
      }
    }
  }
}
```
#### Query all Banks

```
  { 
    allBanks {
      edges {
        node {
          id
          name
          bic
        }
      }
    }
  }
```

#### Query all Partners

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

#### Query all Users

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
