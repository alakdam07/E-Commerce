import React from 'react';
import './App.css';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Home from './components/Home';
import PersonDetail from './components/PersonDetails'

function App() {

  return (

    <React.Fragment>
      <Router>
        <Switch>
          <Route exact path="/" component={Home} />
          <Route exact path="/customer-detail/:id" component={PersonDetail} />
        </Switch>
      </Router>
    </React.Fragment>


  );
}

export default App;
