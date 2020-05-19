import React, { Component } from 'react';
import { BrowserRouter as Router, Route} from 'react-router-dom';
import './app.css';

import Navbar from '../navbar';
import Jumbotron from '../jumbotron';
import { About, Docs } from '../pages';

const App: React.FC = () => {
    return (
        <Router>
            <Navbar />
            <Route path="/" component={Jumbotron} exact></Route>
            <Route path="/docs" component={Docs}></Route>
            <Route path="/about" component={About}></Route>
        </Router>
    );
}

export default App;
