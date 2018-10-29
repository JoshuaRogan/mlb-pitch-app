import React from 'react';
import propTypes from 'prop-types';
import injectSheet from 'react-jss';
import blue from '@material-ui/core/colors/blue';

const styles = {
    container: {

    },
    strikeZone: {
        display: 'grid',
        width: 300,
        height: 450,
        border: {
            size: 2,
            style: 'solid',
            color: blue["500"],
            radius: 5,
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
    };

    render() {
        const { classes } = this.props;
        return <div className={classes.container}>
          <div className={classes.strikeZone}>
              <div><div /> <div /> <div /></div>
              <div><div /> <div /> <div /></div>
              <div><div /> <div /> <div /></div>
          </div>
        </div>;
    }
}

export default injectSheet(styles)(StrikeZone);