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
    fetch("http://localhost:8000/get_all_puzzles/", {
      method: "GET"
    })
      .then(function (response) {
        return response.json();
      })
      .then((data) => {
        this.setState({ puzzles: data });
      });
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
