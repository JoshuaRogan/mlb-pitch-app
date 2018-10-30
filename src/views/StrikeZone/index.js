import {PropTypes} from "@material-ui/core";
import React from 'react';
import propTypes from 'prop-types';
import injectSheet from 'react-jss';
import blue from '@material-ui/core/colors/blue';
import Draggable from 'react-draggable';
import baseball from './../../logo.svg';
import { withTheme } from '@material-ui/core/styles';

const styles = {
    container: {
        textAlign: 'center',
    },
    strikeZone: {
        display: 'grid',
        position: 'relative',
        width: 300,
        height: 450,
        border: {
            size: 2,
            style: 'solid',
            color: blue["500"],
            radius: 5,
        },
        margin: {
            left: 'auto',
            right: 'auto',
        },
        gridTemplateColumns: '1fr 1fr 1fr',
        gridTemplateRows: '1fr 1fr 1fr',
        justifyContent: 'stretch',
    },
};

/**
 * Full re-usable strike zone component
 *   * Pitch location (can have multiple)
 *   * Determines if a pitch location is a strike/ball
 */
class StrikeZone extends React.Component {
    // Simple location
    static propTypes = {
        pitches: propTypes.array,
        onChange: propTypes.func,
    };

    onDragEnd = (mouseEvent, libEvent) => {
        console.log(libEvent);
        this.props.onChange({x: libEvent.x, y: libEvent.y});
    };

    render() {
        const { classes } = this.props;
        return <div className={classes.container}>
          <div className={classes.strikeZone}>
              <Draggable bounds="parent" onStop={this.onDragEnd}>
                  <img alt="baseball" src={baseball} width={25} height={25} draggable={false} />
              </Draggable>
          </div>
        </div>;
    }
}

export default injectSheet(styles)(StrikeZone);
