import React, { Component } from 'react';
import StrikeZone from './views/StrikeZone';
import injectSheet from 'react-jss';
import CssBaseline from '@material-ui/core/CssBaseline';
import Grid from '@material-ui/core/Grid';
import { MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import Paper from '@material-ui/core/Paper';
import classNames from 'classnames';


const theme = createMuiTheme({
    typography: {
        useNextVariants: true,
    },
});

const styles = {
    app: {
        textAlign: 'center',
    },
    main: {
        minHeight: '500px',
    },
    footer: {
        textAlign: 'center',
        width: '100%',
    },
    form: {
        display: 'flex',
        justifyContent: 'space-evenly',
        fallbacks: {
            justifyContent: 'center',
        }
    },
    formContainer: {
        padding: 10,
        width: '100%',
        marginLeft: 10,
        marginBottom: 10,
    },
    input: {
        textAlign: 'center',
        background: 'red',
    }
};

class App extends Component {
    state = {
        mph: 75,
        pitch: {
            x: 0,
            y: 0,
        },
        rpm: 50,
    };

    handleMphChange = (event) => {
        this.setState({mph: event.target.value});
    };

    handleRotationChange = (event) => {
        this.setState({rpm: event.target.value});
    };

    handlePitchChange = (event) => {
        this.setState({pitch: {x: event.x, y: event.y}});
    };

  render() {
    const { app, main, form, formContainer, strikeZone, input } = this.props.classes;
    return (
        <MuiThemeProvider theme={theme}>
            <code>
                {JSON.stringify(this.state)}
            </code>
            <CssBaseline />
            <main className={main}>
                <Paper className={formContainer}>
                    <form className={form}>
                        <TextField
                            label="MPH"
                            value={this.state.mph}
                            onChange={this.handleMphChange}
                            type="number"
                        />
                        <TextField
                            label="RPM"
                            value={this.state.rpm}
                            onChange={this.handleRotationChange}
                            type="number"
                        />
                    </form>
                </Paper>
                <StrikeZone onChange={this.handlePitchChange}/>
            </main>
            <footer>
                <div style={{fontSize: 10}}>Icons made by <a href="http://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank" rel="noopener noreferrer">CC 3.0 BY</a></div>
            </footer>
        </MuiThemeProvider>
    );
  }
}

export default injectSheet(styles)(App);
