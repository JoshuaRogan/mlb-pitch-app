import React from 'react';
import propTypes from 'prop-types';
import blue from '@material-ui/core/colors/blue';
import Draggable from 'react-draggable';

import styled from 'styled-components';

import baseball from '../../logo.svg';

const Container = styled.div`
  text-align: center;
`;

const StrikeZoneStyled = styled.div`
  border-radius: 5px;
  border: 2px solid ${blue['500']};
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr 1fr;
  height: 450px;
  justify-content: stretch; 
  margin-left: auto;
  margin-right: auto;
  position: relative;
  width: 300px;
`;

/**
 * Full re-usable strike zone component
 *   * Pitch location (can have multiple)
 *   * Determines if a pitch location is a strike/ball
 */
class StrikeZone extends React.Component {
  // Simple location
  static propTypes = {
      onChange: propTypes.func,
      pitches: propTypes.array,
  };

  onDragEnd = (mouseEvent, libEvent) => {
      this.props.onChange({ x: libEvent.x, y: libEvent.y });
  };

  render() {
      return (
          <Container>
              <StrikeZoneStyled>
                  <Draggable bounds="parent" onStop={this.onDragEnd}>
                      <img alt="baseball" src={baseball} width={25} height={25} draggable={false} />
                  </Draggable>
              </StrikeZoneStyled>
          </Container>
      );
  }
}

export default StrikeZone;
