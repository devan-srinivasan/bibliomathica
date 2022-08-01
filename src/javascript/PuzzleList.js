import React, { Component } from "react";
import Puzzle from "./Puzzle.js";
import "./react-stylesheets/PuzzleList.css";

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
        className="Puzzle"
        key={index}
        title={puz.title}
        index={index}
        handleClick={this.handleClick.bind(this)}
      />
    ));
    return (
      <div className="PuzzleList">
        <div className="list-header">
          <h2>Puzzles</h2>
          <button onClick={() => this.getPuzzles()}>Refresh</button>
        </div>
        {puzzleItems}
      </div>
    );
  }
}

export default PuzzleList;
