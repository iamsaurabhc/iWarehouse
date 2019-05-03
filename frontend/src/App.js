import React, { Component } from 'react'
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom'
import { ApolloProvider} from 'react-apollo'
import { ApolloClient, InMemoryCache } from "apollo-boost";
import { BatchHttpLink } from 'apollo-link-batch-http';
import CreateClient from './views/CreateClient';
import DetailClient from './views/DetailClient';
import ListView from './views/ListView';
import LoginView from './views/LoginView';
import LogoutView from './views/LogoutView';

const batchLink = new BatchHttpLink({
  uri: 'http://127.0.0.1:8000/gql?',
  batchInterval: 10,
});

const client = new ApolloClient({
  link: batchLink,
  cache: new InMemoryCache(),
  connectToDevTools: process.env.NODE_ENV !== 'production',
  credentials:'same-origin'
});

class App extends Component {
  render() {
    return (
      <ApolloProvider client={client}>
        <Router>
          <div>
            <ul>
              <li><Link to="/">Home</Link></li>
              <li><Link to="/client/create/">Create Client</Link></li>
              <li><Link to="/login/">Login</Link></li>
              <li><Link to="/logout/">Logout</Link></li>
            </ul>
            <Route exact path="/" component={ListView} />
            <Route exact path="/login/" component={LoginView} />
            <Route exact path="/logout/" component={LogoutView} />
            <Switch>
              <Route path="/client/create/" component={CreateClient} />
              <Route path="/client/:id/" component={DetailClient} />
            </Switch>
          </div>
        </Router>
      </ApolloProvider>
    )
  }
}

export default App