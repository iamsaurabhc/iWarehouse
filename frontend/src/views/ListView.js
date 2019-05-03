import React from 'react'
import { Link } from 'react-router-dom'
import { graphql } from 'react-apollo'
import { gql } from 'apollo-boost'


const query = gql`
{
  allClients{clientID,clientName,clientPhone,clientAddress}
}
`

class ListView extends React.Component {
  render() {
    let { data } = this.props
    if (data.loading || !data.allClients) {
      return <div>Loading...</div>
    }

    return (
      <div>
        {data.allClients.map(client => (
          <p key={client.clientID}>
            <Link to={`/client/${client.clientID}/`}>
              {client.clientName}, {client.clientPhone}, {client.clientAddress}
            </Link>
          </p>
        ))}
      </div>
    )
  }
}

ListView = graphql(query)(ListView)
export default ListView
