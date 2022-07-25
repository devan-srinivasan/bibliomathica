import React, { Component } from "react";

class Puzzle extends Component {
  constructor(props) {
    super(props);
  }

  handleClick() {
    this.props.handleClick({
      title: this.props.title,
      index: this.props.index
    });
  }

  render() {
    return (
      <div className="Puzzle">
        <button className="puzzle-button" onClick={() => this.handleClick()}>
          {this.props.title}
        </button>
      </div>
    );
  }
}

export default Puzzle;
