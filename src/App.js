import React, { Component } from 'react';

import CssBaseline from '@material-ui/core/CssBaseline';
import { MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import Paper from '@material-ui/core/Paper';
import styled from 'styled-components';

import StrikeZone from './views/StrikeZone';

const theme = createMuiTheme({
    typography: {
        useNextVariants: true,
    },
});

const Main = styled.main`
  min-height: 500px;
`;

const Footer = styled.div`
  text-align: center;
  width: 100%;
`;

const FormContainer = styled(Paper)`
  padding: 10px;
  width: 100%;
  margin-left: 10px;
  margin-bottom: 10px;
`;

const Form = styled.form`
  display: flex;
  justify-content: center;
  justify-content: space-evenly;
`;

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
        this.setState({ mph: event.target.value });
    };

    handleRotationChange = (event) => {
        this.setState({ rpm: event.target.value });
    };

    handlePitchChange = (event) => {
        this.setState({ pitch: { x: event.x, y: event.y } });
    };

    render() {
        return (
            <MuiThemeProvider theme={theme}>
                <code>
                    {JSON.stringify(this.state)}
                </code>
                <CssBaseline />
                <Main>
                    <FormContainer>
                        <Form>
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
                        </Form>
                    </FormContainer>
                    <StrikeZone onChange={this.handlePitchChange} />
                </Main>
                <Footer>
                    <div style={{ fontSize: 10 }}>
Icons made by
                        <a href="http://www.freepik.com" title="Freepik">Freepik</a>
                        {' '}
from
                        <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a>
                        {' '}
is licensed by
                        <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank" rel="noopener noreferrer">CC 3.0 BY</a>
                    </div>
                </Footer>
            </MuiThemeProvider>
        );
    }
}

export default App;
