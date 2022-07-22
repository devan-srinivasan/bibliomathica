import React, { Component } from "react";
import Puzzle from "./Puzzle.js";

class PuzzleList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      puzzles: []
    };
  }

  handleClick(puz) {
    this.props.handleClick(this.state.puzzles[puz.index]);
  }

  getPuzzles() {
    //TODO this is temporary will need to actually fetch puzzles
    var puzzles = [
      {
        title: "p1",
        question: "2+2"
      },
      {
        title: "p2",
        question: "3+3"
      },
      {
        title: "p3",
        question: "4+4"
      }
    ];

    this.setState({ puzzles: puzzles });
  }

  render() {
    const puzzleItems = this.state.puzzles.map((puz, index) => (
      <Puzzle
        key={index}
        title={puz.title}
        index={index}
        handleClick={this.handleClick.bind(this)}
      />
    ));
    return (
      <div className="PuzzleList">
        <button onClick={() => this.getPuzzles()}>Load Puzzles</button>
        {puzzleItems}
      </div>
    );
  }
}

export default PuzzleList;
