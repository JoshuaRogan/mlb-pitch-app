import React, { Component } from 'react';
import StrikeZone from './views/StrikeZone';
import './App.css';
import injectSheet from 'react-jss';
import CssBaseline from '@material-ui/core/CssBaseline';

const styles = {
    app: {
        textAlign: 'center',
    },
};

class App extends Component {
  render() {
    return (
      <div className={this.props.classes.app}>
          <CssBaseline />
          <header className="App-header">
              <StrikeZone />
              <div style={{fontSize: 10}}>Icons made by <a href="http://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank" rel="noopener noreferrer">CC 3.0 BY</a></div>
          </header>
      </div>
    );
  }
}

export default injectSheet(styles)(App);
